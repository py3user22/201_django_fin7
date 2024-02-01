from django.db import models

# Create your models here.

#201 date model demo1
class DateNow(models.Model):
    today_date = models.DateField()
    def __str__(self):
        return self.today_date

class Booking(models.Model):
    first_name = models.CharField(max_length=130)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    def __str__(self):
        return self.first_name




# 0131 demo try of models
class Solar(models.Model):
    Choices = [ ("Mono", "Mono-crystalline"), ("Poly", "Poly-crystalline") ]
    Wires = [ ("12AGW", "12-gauge wiring"), ("10AGW", "10-gauge wiring"), ("8AGW", "8-gauge wiring") ]

    name = models.CharField(max_length=150, primary_key=True)
    type = models.CharField(max_length=4, choices=Choices)
    #price = models.IntegerField(default=500)
    description = models.CharField(max_length=240, default="Decription and details", blank=True )
    comments = models.CharField(max_length=150, default="Any additional notes:", blank=True )
    parts_ID = models.CharField(max_length=15)
