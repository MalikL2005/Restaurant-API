from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self): 
        return f'{self.id} - {self.name} ({self.no_of_guests}) on {self.bookingDate}'

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    def __str__(self):
        return f'{self.id} - {self.title} ({self.price}$); Inventory: {self.inventory}'
    
