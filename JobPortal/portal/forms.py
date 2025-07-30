from django import forms
from django.contrib.auth.models import User
from .models import Profile,Job, Application, UserPermission
from ckeditor.widgets import CKEditorWidget


class UserRegisterForm(forms.Form):

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data
    
    
class JobForm(forms.ModelForm):
    about_job = forms.CharField(widget=CKEditorWidget())
    job_requirement = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Job
        fields = [
            'title', 'company_name','about_job', 'job_requirement','job_type',  
            'exp_level','location', 'salary_range','vacancy', 'deadline'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Senior Frontend Developer'}),
            'company_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Tech Innovations Inc.'}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
            'exp_level': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. San Francisco, CA'}),
            'salary_range': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. $80,000 - $120,000'}),
            'vacancy': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g..'}),
            'deadline': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'experience', 'resume', 'cover_letter']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'john@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+8801XXXXXXXXX'}),
            'address': forms.Textarea(attrs={'class': 'form-input', 'rows': 2, 'placeholder': '123 Main St'}),
            'experience': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Years of Experience'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Write your cover letter...'}),
        }

class UserPermissionForm(forms.ModelForm):
    class Meta:
        model = UserPermission
        fields = ['user', 'menu', 'can_view', 'can_add', 'can_update', 'can_delete']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'menu': forms.Select(attrs={'class': 'form-control'}),
        }