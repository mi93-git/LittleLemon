from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)                 # Name varchar(255)
    no_of_guests = models.PositiveIntegerField()            # No_of_guests int(6)
    booking_date = models.DateTimeField()                   # BookingDate datetime
    
class Menu(models.Model):
    title = models.CharField(max_length=255)                # Title varchar(255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price decimal(10,2)
    inventory = models.PositiveSmallIntegerField()          # Inventory int(5)             