from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        field = ['username','passsword']
        widgets = {"password": forms.PasswordInput()}