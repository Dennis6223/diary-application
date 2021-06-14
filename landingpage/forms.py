from django import forms
from django.forms import ModelForm
from .models import Diary

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class diaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields= '__all__'
        exclude =['diary_time_created']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['diary_editor'].widget.attrs.update({'class':'textarea','placeholder':'Hello, there! Whats on your mind?'})
        self.fields['diary_editor'].widget.attrs['cols'] = 100
        self.fields['diary_editor'].widget.attrs['rows'] = 10
        self.fields['diary_editor'].widget.attrs['size'] = 20

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    