from portal.models import UserPermission,Job, Application, InterviewSchedule
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone


def checkUserPermission(request, access_type, menu_url):
    try:
        user_permissions = {
            "can_view": "can_view",
            "can_add": "can_add",
            "can_update": "can_update",
            "can_delete": "can_delete",
        }

        if request.user.is_superuser: return True

        check_user_permission = UserPermission.objects.filter(
            user_id=request.user.id, is_active=True, **{user_permissions[access_type]: True}, menu__menu_url=menu_url,
        )
 
        if check_user_permission: return True
        else: return False
    except:
        return False
    

# def send_mail(request):
#     subject = f"Interview Schedule for {request.job.title}"
#     message= render_to_string('candidates/interview_schedule_mail.html', {'request':request}) 
#     to = request.email
#     send_email = EmailMultiAlternatives(subject, '', to=to)
#     send_email.attach_alternative(message, "text/html")
#     send_email.save()

def send_mail(candidate):
    subject = f"Interview Schedule for {candidate.job.title}"
    message = render_to_string('candidates/interview_schedule_mail.html', {'candidate': candidate}) 
    to = [candidate.email]
    send_email = EmailMultiAlternatives(subject, '', to=to)
    send_email.attach_alternative(message, "text/html")
    send_email.send()



def deactivate_expired_jobs_and_applications():
    expired_jobs = Job.objects.filter(deadline__lt=timezone.now(), is_active=True)

    for job in expired_jobs:
        job.is_active = False
        job.save()

        applications = Application.objects.filter(job=job, is_active=True)
        applications.update(is_active=False)

def deactivate_expired_interview_schedule():
    expired_interview_schedule = InterviewSchedule.objects.filter(schedule_time__lt=timezone.now())

    for schedule in expired_interview_schedule:
        schedule.is_deleted = True
        schedule.save()