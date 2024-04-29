from django.db import models
from organisations.models import Organisation

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    organization = models.ForeignKey(Organisation, related_name='locations', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organisation, related_name='animals', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class FarmerProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    locations = models.ManyToManyField(Location, related_name='farmers')
    animals = models.ManyToManyField(Animal, related_name='farmers')
    organization = models.ForeignKey(Organisation, related_name='farmers', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
