from django.shortcuts import render


# Home Page
def home(request):
    return render(request, "core/home.html")


# Doctors Page
def doctors(request):
    return render(request, "core/doctors.html")


def doctor_login(request):
    return render(request, "core/doctor_login.html")


def doctor_register(request):
    return render(request, "core/doctor_register.html")


def doctor_dashboard(request):
    return render(request, "core/doctor_dashboard.html")


# Services Page
def services(request):
    return render(request, "core/services.html")


# Appointments Page
def appointments(request):
    return render(request, "core/appointments.html")


# Contact Page
def contact(request):
    return render(request, "core/contact.html")


# Emergency Page
def emergency(request):
    return render(request, "core/emergency.html")


# Patient Module
def patient_login(request):
    return render(request, "core/patient_login.html")


def patient_register(request):
    return render(request, "core/patient_register.html")


def patient_dashboard(request):
    return render(request, "core/patient_dashboard.html")