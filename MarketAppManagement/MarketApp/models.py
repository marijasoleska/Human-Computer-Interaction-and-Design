from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):
    TYPE=[
        ("H","HRANA"),
        ("P","PIJALAK"),
        ("PE","PEKARA"),
        ("K","KOZMETIKA"),
        ("HI","HIGIENA")
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=2, choices=TYPE)
    homemade=models.BooleanField(default=False)
    code=models.TextField()
    def __str__(self):
        return f"{self.name} {self.type}"

class ContactInfo(models.Model):
    street=models.CharField(max_length=100)
    street_number=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.street} {self.street_number}"

class Market(models.Model):
    name = models.CharField(max_length=100)
    num_of_markets=models.IntegerField()
    date_of_opening=models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_time_from=models.TimeField()
    work_time_to=models.TimeField()
    info=models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    embg=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.IntegerField()
    market=models.ForeignKey(Market, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} {self.surname}"


class ProductInMarket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return f"{self.product.name} {self.market.name}"