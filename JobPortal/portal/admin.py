from django.contrib import admin
from .models import Job, InterviewSchedule, Application, MenuList, UserPermission
# Register your models here.
admin.site.register(Job)
admin.site.register(MenuList)
admin.site.register(UserPermission)