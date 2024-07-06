from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='About_us'),
    path('contact/', views.contact, name='Contact_us'),

    path('patient_list/', views.patient_list, name='patient_list'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),

    path('patient_click/', views.patient_click, name='patient_click'),
    path('patient_signup/', views.patient_signup, name='patient_signup'),
    path('patient_signin/', views.patient_signin, name='patient_signin'),

    path('doctor_list/', views.doctor_list, name='doctor_list'),
    path('doctor_click/', views.doctor_click, name='doctor_click'),
    path('doctor_signup/', views.doctor_signup, name='doctor_signup'),
    path('doctor_signin/', views.doctor_signin, name='doctor_signin'),
    #path('admin_add_appointment/', views.admin_add_appointment,name='admin_add_appointment'),

    path('homenew/', views.homenew, name='homenew'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),

    path('admin_click/', views.admin_click, name='admin_click'),
    path('admin_signin/', views.admin_signin, name='admin_signin'),

]
