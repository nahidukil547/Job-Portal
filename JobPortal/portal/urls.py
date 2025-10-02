from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('applicants/', views.candidate_list, name='candidate_list'),
    path('schedules/', views.interview_schedule_list, name='interview_schedule_list'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('create/jobs/', views.create_job, name='create_job'),

    path('job/details/<slug:slug>/', views.job_details, name='job_details'),
    path('job/update/<slug:slug>/', views.update_job, name='update_job'),
    path('job/delete/<slug:slug>/', views.delete_job, name='delete_job'),

    path('candidate/details/<int:id>/', views.candidate_details, name='candidate_details'),
    path('candidate/delete/<int:id>/', views.candidate_delete, name='candidate_delete'),

    path('schedule/delete/<int:id>/', views.delete_interview_schedule, name='delete_interview_schedule'),

    path('user/access/', views.user_permission_list, name='user_permission_list'),
    path('user/access/create/', views.create_permission, name='create_permission'),
    path('user/access/update/<int:id>', views.update_user_permission, name='update_user_permission'),
    path('user/access/delete/<int:id>', views.delete_user_permission, name='delete_user_permission'),


    path('approve/job/<int:id>/', views.approve, name='approve'),
    path('reject/job/<int:id>/', views.reject, name='reject'),

    path('employees/', views.employee_list, name='employee_list'),
    path('approve/job/<int:id>/', views.approve, name='approve'),
    path('reject/job/<int:id>/', views.reject, name='reject'),

]
