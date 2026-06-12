from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('doctors/', views.doctors),
    path('doctor-login/', views.doctor_login),
    path('doctor-register/', views.doctor_register),
    path('doctor-dashboard/', views.doctor_dashboard),

    path('services/', views.services),
    path('appointments/', views.appointments),
    path('contact/', views.contact),
    path('emergency/', views.emergency),

    path('patient-login/', views.patient_login),
    path('patient-register/', views.patient_register),
    path('patient-dashboard/', views.patient_dashboard),
]