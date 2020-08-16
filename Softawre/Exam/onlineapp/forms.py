from django import forms

from .models import Student,Teacher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("__all__")

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("__all__")
