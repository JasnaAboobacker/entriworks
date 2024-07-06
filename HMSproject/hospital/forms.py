from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from . import models
from .models import Doctor, Patient, Appointment




class PatientSignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))






class DoctorSignupForm(UserCreationForm):
    d_name = forms.CharField(max_length=50)
    mobile = forms.CharField(max_length=15)
    specialization = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('d_name', 'email', 'password1', 'password2', 'mobile', 'specialization')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            doctor = Doctor(user=user,d_name=self.cleaned_data['d_name'],mobile=self.cleaned_data['mobile'], specialization=self.cleaned_data['specialization'])
            doctor.save()
        return user


class PatientSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    address = forms.CharField(widget=forms.Textarea)
    mobile = forms.CharField(max_length=15)
    gender = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            patient = Patient(user=user, name=self.cleaned_data['name'], address=self.cleaned_data['address'], mobile=self.cleaned_data['mobile'], gender=self.cleaned_data['gender'])
            patient.save()
        return user

class DoctorSignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AdminSignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))




