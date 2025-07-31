from django.shortcuts import render
from .models import UserPermission, Profile, Job, Application, InterviewSchedule
from .common_fun import checkUserPermission,send_mail, deactivate_expired_jobs_and_applications, deactivate_expired_interview_schedule
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib import messages
from .forms import UserRegisterForm, JobForm,ApplicationForm, UserPermissionForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
# Create your views here.

def home(request): 
    query = request.GET.get('query', '').strip()
    job_type = request.GET.getlist('job_type')
    exp_level = request.GET.getlist('exp_level')
    salary_range = request.GET.getlist('salary_range')

    jobs = Job.objects.filter(is_deleted=False, is_active=True)

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(company_name__icontains=query) |
            Q(job_type__icontains=query) |
            Q(exp_level__icontains=query)
        )

    if job_type:
        jobs = jobs.filter(job_type__in=job_type)

    if exp_level:
        jobs = jobs.filter(exp_level__in=exp_level)

    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    job_type_choices = [
        ('full-time', 'Full Time'),
        ('part-time', 'Part Time'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
    ]

    exp_level_choices = [
        ('entry-level', 'Entry Level'),
        ('mid-level', 'Mid Level'),
        ('senior-level', 'Senior Level'),
        ('intern', 'Intern'),
    ]

    context = {
        'query': query,
        'page_obj': page_obj,
        'jobs': page_obj.object_list,
        'selected_job_type': job_type,
        'selected_exp_level': exp_level,
        'selected_salary_range': salary_range,
        'job_type_choices': job_type_choices,
        'exp_level_choices': exp_level_choices,
    }
    deactivate_expired_jobs_and_applications()
    return render(request, 'home/index.html', context)



def dashboard(request):
    if not checkUserPermission(request, "can_view", "dashboard/"):
        return redirect('home')
    query = request.GET.get('q', '').strip()  
    jobs = Job.objects.filter(is_deleted=False, is_active=True)

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(company_name__icontains=query) |
            Q(job_type__icontains=query) |
            Q(exp_level__icontains=query)
        )

    paginator = Paginator(jobs, 4)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    candidates = Application.objects.filter(job__in=jobs).order_by('-applied_at')

    context = {
        'query': query,
        'page_obj': page_obj,
        'jobs': page_obj.object_list,
        'candidates': candidates,
    }

    return render(request, 'dashboard/dashboard.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']  
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=email,  
                email=email,
                password=password
            )

            Profile.objects.create(
                user=user,
                phone=phone,
                address=address,
                is_active=False
            )

            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'auth/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'auth/login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('login')


def create_job(request):
    if not checkUserPermission(request, "can_add", "dashboard/"):
        return redirect('dashboard')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            return redirect('dashboard')  
    else:
        form = JobForm()
    
    return render(request, 'jobs/create_job.html', {'form': form})



def job_details(request, slug):
    
    job = get_object_or_404(Job, slug=slug)
    candidates = Application.objects.filter(job=job).order_by('-applied_at')

    if request.method =="POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Application.objects.filter(job=job, email=email):
                messages.warning(request, 'You have already applied for this job with this email.')
                return redirect('job_details', slug=job.slug)
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('home')

    form = ApplicationForm()

    context = {
        'job': job,
        'candidates': candidates,
        'form':form
    }
    
    if not request.user.is_authenticated:
        return render(request, 'jobs/job_details_with_apply.html', context)
    
    if not checkUserPermission(request, "can_view", "dashboard/"):
        return render(request, 'jobs/job_details_with_apply.html', context)

    return render(request, 'jobs/job_details.html', context)

@login_required
def update_job(request, slug):
    if not checkUserPermission(request, "can_update", "dashboard/"):
        return redirect('dashboard')
    
    job = get_object_or_404(Job, slug=slug)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_details', slug=job.slug)
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/update_job.html', {
        'form': form,
        'job': job,
    })
@login_required
def delete_job(request, slug):
    if not checkUserPermission(request, "can_delete", "dashboard/"):
        return redirect('dashboard')
    job = get_object_or_404(Job, slug=slug, is_deleted=False)
    
    job.is_deleted = True
    job.save()

    return redirect('dashboard')


def candidate_details(request, id):
    if not checkUserPermission(request, "can_view", "applicants/"):
        return redirect('home')
    
    candidate = get_object_or_404(Application, id=id)

    if request.method == "POST":
        interview_date = request.POST.get('interview-date')
        interview_time = request.POST.get('interview-time')
        model = request.POST.get('interview-model')
        location = request.POST.get('interview-location')

        if not all([interview_date, interview_time, model, location]):
            messages.error(request, "All interview fields are required.")
            return redirect('candidate_details', id=id)

        try:
            datetime_str = f"{interview_date} {interview_time}"
            schedule_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            schedule_datetime = timezone.make_aware(schedule_datetime)
        except ValueError as e:
            messages.error(request, "Invalid date/time format. Please use correct format.",{e})
            return redirect('candidate_details', id=id)

        # if InterviewSchedule.objects.filter(applicant=candidate, job=candidate.job).exists():
        #     messages.warning(request, "An interview has already been scheduled for this candidate.")
        #     return redirect('candidate_details', id=id)

        InterviewSchedule.objects.create(
            applicant=candidate,
            job=candidate.job,
            schedule_date=interview_date,
            schedule_time=schedule_datetime,
            interview_model=model,
            interview_location=location,
            created_by=request.user
        )
        send_mail(candidate)
        messages.success(request, "Interview scheduled successfully.")
        return redirect('dashboard')

    return render(request, 'candidates/candidate_details.html', {'candidate': candidate})


def candidate_list(request):
    if not checkUserPermission(request, "can_view", "applicants/"):
        return redirect('home')
    
    candidate= Application.objects.filter(is_active=True, is_deleted=False)
    paginator = Paginator(candidate, 4)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        
        'page_obj': page_obj,
        'jobs': page_obj.object_list,
        'candidates': candidate,
    }
    return render(request, 'candidates/candidate_list.html',context)


def candidate_delete(request, id):
    if not checkUserPermission(request, "can_delete", "applicants/"):
        return redirect('candidate_list')
    candidate= get_object_or_404(Application, id= id)
    candidate.is_active= False
    candidate.is_deleted=True
    candidate.save()
    return redirect('candidate_list')


def user_permission_list(request):
    if not checkUserPermission(request, "can_view", "user/access/"):
        return redirect('home')
    permission=UserPermission.objects.filter(is_active=True, deleted= False)
    return render(request, 'permissions/user_permission.html',{'permission':permission})

def create_permission(request):
    if not checkUserPermission(request, "can_add", "user/access/"):
        return redirect('home')
    if request.method == 'POST':
        form = UserPermissionForm(request.POST)
        if form.is_valid():
            permission = form.save(commit=False)
            permission.created_by = request.user
            permission.save()
            return redirect('user_permission_list') 
    else:
        form = UserPermissionForm()
    return render(request, 'permissions/create_permission.html', {'form': form})


def update_user_permission(request,id):
    if not checkUserPermission(request, "can_update", "user/access/"):
        return redirect('home')
    form= get_object_or_404(UserPermission, id=id)
    if request.method == 'POST':
        form = UserPermissionForm(request.POST, instance=form)
        if form.is_valid():
            form.save()
            return redirect('user_permission_list')
    else:
        form = UserPermissionForm(instance=form)
    return render(request,'permissions/update_permission.html', {'form':form})

def delete_user_permission(request,id):
    if not checkUserPermission(request, "can_delete", "user/access/"):
        return redirect('home')
    permission= get_object_or_404(UserPermission, id=id)
    permission.can_add = False
    permission.can_add = False
    permission.can_delete = False
    permission.can_update = False
    permission.is_active = False
    permission.deleted= True
    permission.save()
    return redirect('user_permission_list')



def interview_schedule_list(request):
    if not checkUserPermission(request, "can_view", "schedules/"):
        return redirect('home')
    
    schedule= InterviewSchedule.objects.filter(is_deleted=False)
    deactivate_expired_interview_schedule()
    return render(request, 'candidates/interview_schedule_list.html', {'candidates':schedule})

def delete_interview_schedule(request,id):
    schedule= get_object_or_404(InterviewSchedule, id=id)
    schedule.is_deleted= True
    schedule.save()
    return redirect('interview_schedule_list')

# live test requirement
# @login_required
# def manage_applications(request, job_id):
#     job = get_object_or_404(Job, id=job_id, employer=request.user)

#     if request.method == 'POST':
#         app_id = request.POST.get('application_id')
#         new_status = request.POST.get('status')
#         application = get_object_or_404(Application, id=app_id, job=job)
#         if new_status in dict(Application.STATUS_CHOICES).keys():
#             application.status = new_status
#             application.save()

#     applications = Application.objects.filter(job=job)
#     return render(request, '', {
#         'job': job,
#         'applications': applications
#     })

# @login_required
# def my_applications(request):
#     status_filter = request.GET.get('status', '')
#     apps = Application.objects.filter(applicant=request.user)
#     if status_filter in dict(Application.STATUS_CHOICES).keys():
#         apps = apps.filter(status=status_filter)

#     return render(request, '', {
#         'applications': apps,
#         'status_filter': status_filter,
#         'status_choices': Application.STATUS_CHOICES,
#     })
