from tkinter.tix import Balloon

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pilot(models.Model):
    RANK=[
        ("J","Junior"),
        ("I","Intermediate"),
        ("S","Senior"),
    ]
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    hours_of_flight=models.DecimalField(decimal_places=2, max_digits=3)
    position=models.CharField(max_length=1,choices=RANK)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Baloon(models.Model):
    TYPES=[
        ("S","Small Baloon"),
        ("M","Medium Baloon"),
        ("L","Large Baloon"),
    ]
    type=models.CharField(max_length=1,choices=TYPES)
    distributed=models.CharField(max_length=100)
    num_of_passengers=models.IntegerField()

    def __str__(self):
        return f"{self.type} {self.distributed}"

class Airline(models.Model):
    name=models.CharField(max_length=100)
    year_founded=models.DateField()
    outside_of_europe=models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.year_founded}"

class Flight(models.Model):
    code=models.CharField(max_length=100)
    airport_takeoff=models.CharField(max_length=100)
    airport_landing=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    date=models.DateField()
    baloon=models.ForeignKey(Baloon, on_delete=models.CASCADE)
    pilot=models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline=models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.airport_takeoff}"

class AirlinePilot(models.Model):
    pilot=models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline=models.ForeignKey(Airline, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.pilot} {self.airline}"