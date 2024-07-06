from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import models
from .forms import PatientSignUpForm, DoctorSignupForm
from .models import Patient, Appointment, Doctor


# Create your views here

@login_required
def homenew(request):
    if request.user.is_doctor:
        return redirect('doctor_dashboard')
    elif request.user.is_patient:
        return redirect('patient_dashboard')
    else:
        return redirect('admin_dashboard')


@login_required
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')


@login_required
def doctor_dashboard(request):
    doctor = Doctor.objects.get(user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'doctors/doctor_dashboard.html', {'doctor': doctor, 'appointments': appointments})


@login_required
def patient_dashboard(request):
    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        patient = None
    return render(request, 'patients/patient_dashboard.html', {'patient': patient})


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})


@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})


def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, 'Signup successful!')
            return redirect('home')
    else:
        form = PatientSignUpForm()
    return render(request, 'patients/patient_signup.html', {'form': form})


def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.doctor.mobile = form.cleaned_data.get('mobile')
            user.doctor.specialization = form.cleaned_data.get('specialization')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Signup successful!')
                return redirect('home')  # Ensure 'home' is defined in your URLs
            else:
                messages.error(request, 'Authentication failed. Please try again.')
    else:
        form = DoctorSignupForm()
    return render(request, 'doctors/doctor_signup.html', {'form': form})


def patient_signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('patient_dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'patients/patient_signin.html', {'form': form})


def doctor_signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('doctor_dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'doctors/doctor_signin.html', {'form': form})


def patient_click(request):
    return render(request, 'patients/patient_click.html')


@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})


def doctor_click(request):
    return render(request, 'doctors/doctor_click.html')


def admin_click(request):
    return render(request, 'admin/admin_click.html')


def admin_signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'admin/admin_signin.html', {'form': form})
