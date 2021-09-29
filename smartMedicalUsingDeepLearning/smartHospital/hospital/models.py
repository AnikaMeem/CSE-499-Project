from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    hospital = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=False,default="",unique=True)
    password = models.CharField(max_length=30,null=False,default="")
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(Doctor, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.first_name

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100,null=False,default="",unique=True)
    password = models.CharField(max_length=40,null=False,default="")

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name

class Appointment(models.Model):
    patient = models.IntegerField(null=False,default=-1)
    doctor  = models.IntegerField(null=False,default=-1)
    date = models.CharField(max_length=40,null=False,default="01/01/1970")
    approved = models.BooleanField(default=False,null=False)
    
    def __str__(self):
        return self.date

class Disease(models.Model):
    diseaseName = models.CharField(max_length=40,null=False,default="No Disease",unique=True)

    def __str__(self):
        return self.diseaseName