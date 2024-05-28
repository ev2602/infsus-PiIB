from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=30)

class Bicycle(Product):
    model = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class RentBicycle(Bicycle):
    reservedDates = ArrayField(models.DateField(), default=list)
    pricePerDay = models.FloatField()

class SaleBicycle(Bicycle):
    price = models.FloatField()
    availability = models.IntegerField()

class Equipment(Product):
    name = models.CharField(max_length=30)

class RentEquipment(Equipment):
    reservedDates = ArrayField(models.DateField(), default=list)
    pricePerDay = models.FloatField()

class SaleEquipment(Equipment):
    price = models.FloatField()
    availability = models.IntegerField()

class Reservation(models.Model):
    oib = models.CharField(max_length=9)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class ReservationRent(Reservation):
    reservedDates = ArrayField(models.DateField(), default=list)

class ReservationSale(Reservation):
    dateToCollect = models.DateField()