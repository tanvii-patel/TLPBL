from django import forms
from .models import Timetable, Task, Resource
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['subject', 'day', 'start_time', 'end_time', 'notes']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'title', 'due_date', 'completed']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'image', 'file']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
