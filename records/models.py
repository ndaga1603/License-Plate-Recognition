from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class Vehicle(models.Model):
    type_choices = [
        ('Personal', 'Personal'),
        ('Commercial', 'Commercial'),
        ('Government', 'Government'),
    ]
    
    staus_choices = [
        ('Clean', 'Clean'),
        ('Dept', 'Dept'),
    ]
    
    plate_number = models.CharField(max_length=10)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=type_choices)
    status = models.CharField(max_length=10, choices=staus_choices)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.model + ' ' + self.plate_number
