from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from doctors.models import Doctor

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other')
    address = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients', null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('patient', 'doctor')  # prevent duplicates

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
