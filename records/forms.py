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
            "type": forms.TextInput(attrs={"class": "form-control"}),
        }

    # def validate_plate_number(self):
    #     plate_number = self.cleaned_data["plate_number"]
    #     print(plate_number)
    #     if Vehicle.objects.filter(plate_number=plate_number).exists():
    #         print("Plate number exists")
    #         raise forms.ValidationError("This plate number is already in use")
    #     return plate_number

    # def validate_owner(self):
    #     owner = self.cleaned_data["owner"]
    #     print(owner)
    #     if Owner.objects.filter(owner=owner).exists():
    #         return owner
    #     else:
    #         print("Owner does not exist")
    #         raise forms.ValidationError("This owner does not exist")

    # def form_valid(self, form):
    #     owner = form.validate_owner()
    #     plate_number = form.validate_plate_number()
    #     form.instance.owner = owner
    #     form.instance.plate_number = plate_number
    #     form.save()
    #     return super().form_valid(form)


class RecognitionForm(forms.Form):
    license_plate = forms.ImageField()
 