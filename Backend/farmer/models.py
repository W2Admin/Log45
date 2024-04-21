from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    animals = models.ManyToManyField(Animal)
    # Add more fields as needed

    def __str__(self):
        return self.name
