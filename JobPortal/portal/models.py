from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime
from django.utils import timezone
from datetime import timedelta
from ckeditor.fields import RichTextField
# Create your models here.
class MenuList(models.Model):
    module_name        = models.CharField(max_length=100, db_index=True)
    menu_name          = models.CharField(max_length=100, unique=True, db_index=True)
    menu_url           = models.CharField(max_length=250, unique=True)
    menu_icon          = models.CharField(max_length=250, blank=True, null=True)
    parent_id          = models.IntegerField(null=True, blank=True)
    is_main_menu       = models.BooleanField(default=False)
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(blank=True, null=True)
    deleted_at         = models.DateTimeField(blank=True, null=True)
    created_by         = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active          = models.BooleanField(default=True)
    deleted            = models.BooleanField(default=False)

    class Meta:
        db_table = "menu_list"

    def __str__(self) -> str:
        return self.menu_name

class UserPermission(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employee_user_for_permission") 
    menu          = models.ForeignKey(MenuList, on_delete=models.CASCADE, related_name="menu_for_permission") 
    can_view      = models.BooleanField(default=False)
    can_add       = models.BooleanField(default=False)
    can_update    = models.BooleanField(default=False)
    can_delete    = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    created_by    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by_user") 
    updated_by    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_by_user", blank=True, null=True) 
    deleted_by    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deleted_by_user", blank=True, null=True)
    is_active     = models.BooleanField(default=True)
    deleted       = models.BooleanField(default=False)

    class Meta:
        db_table = "user_permission"

    def __str__(self):
        return str(self.menu)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)
    role= models.CharField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user.username

class Job(models.Model):
    JOB_TYPE=(
        ('full-time', 'Full Time'),
        ('part-time', 'Part Time'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
    )
    EXP_LEVEL=(
        ('entry-level', 'Entry Level'),
        ('mid-level', 'Mid Level'),
        ('senior-level', 'Senior Level'),
        ('intern', 'Intern'),
    )
    def default_deadline():
        return timezone.now() + timedelta(days=30)
    
    title = models.CharField(max_length=255)
    slug= models.SlugField(max_length=150, unique=True, blank=True)
    company_name = models.CharField(max_length=255)
    about_job = RichTextField(null=True, blank=True)
    job_requirement = RichTextField(null=True, blank=True)
    salary_range= models.CharField(default="Negotiable", null=True, blank=True, max_length=50)
    job_type=models.CharField(max_length=20, choices=JOB_TYPE)
    exp_level=models.CharField(max_length=30, choices=EXP_LEVEL)
    vacancy= models.PositiveIntegerField(default=1,null=True, blank=True)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(default=default_deadline, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active= models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Job.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

class Application(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=15)
    job = models.ForeignKey(Job, on_delete=models.CASCADE,related_name='applications')
    experience = models.PositiveIntegerField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/')
    status= models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    is_active=models.BooleanField(default=True)
    is_deleted= models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
    
class InterviewSchedule(models.Model):
    
    INT_PLACE=(
        ('on-site', 'On Site'),
        ('online', 'Online'),
    )
    applicant= models.ForeignKey(Application, on_delete=models.CASCADE, related_name='interview_schedule')
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    schedule_date= models.DateField(null=True, blank=True)
    schedule_time= models.DateTimeField(null=True, blank=True)
    interview_model = models.CharField(max_length=30, choices=INT_PLACE, default='on-site')
    interview_location = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted= models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.applicant.first_name} - Schedule"


# live test requirement
# class Application(models.Model):
#     STATUS_CHOICES = (
#         ('pending', 'Pending'),
#         ('approved', 'Approved'),
#         ('rejected', 'Rejected'),
#     )

#     applicant = models.ForeignKey(User, on_delete=models.CASCADE)
#     job = models.ForeignKey(Job, on_delete=models.CASCADE)
#     resume = models.FileField(upload_to='resumes/')
#     cover_letter = models.TextField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     applied_at = models.DateTimeField(auto_now_add=True)



