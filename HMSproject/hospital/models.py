from os import name

from django.contrib.auth.models import User
from django.db import models


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    d_name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.user.d_name




class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username
        # return '{}'.format(self.name)


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.patient.name}'s appointment on {self.appointment_date}"
