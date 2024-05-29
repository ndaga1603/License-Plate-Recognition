from .models import Owner, Vehicle
from django import forms


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ["first_name", "last_name", "email", "phone"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["owner", "status", "model", "plate_number", "type"]
        widgets = {
            "owner": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "model": forms.TextInput(attrs={"class": "form-control"}),
            "plate_number": forms.TextInput(attrs={"class": "form-control"}),
            "type": forms.Select(attrs={"class": "form-control"}),
        }

class RecognitionForm(forms.Form):
    license_plate = forms.ImageField()
