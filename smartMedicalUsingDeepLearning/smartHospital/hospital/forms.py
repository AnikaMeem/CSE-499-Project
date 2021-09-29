from django import forms
from .models import Doctor,Patient

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "hospital": "Hospital",
            "email": "Your Email",
            "password": "Your Password"
        }
        error_messages = {
            "first_name": {
              "required": "Your first name must not be empty!"
            },
            "last_name": {
              "required": "Your last name must not be empty!"
            },
            "hospital": {
              "required": "Your hospital name must not be empty!"
            },
            "email": {
              "required": "Email is required"
            },
            "password":{
                "required": "You must need to provide a password"
            }
        }
        widgets={
            "password":forms.PasswordInput()
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Your Email",
            "password": "Your Password"
        }
        error_messages = {
            "first_name": {
              "required": "Your first name must not be empty!"
            },
            "last_name": {
              "required": "Your last name must not be empty!"
            },
            "email": {
              "required": "Email is required"
            },
            "password":{
                "required": "You must need to provide a password"
            }
        }
        widgets={
            "password":forms.PasswordInput()
        }
