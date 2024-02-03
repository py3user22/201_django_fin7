from django.db import models

# Create your models here.

#201 added menu model
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default='')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'b_app201_menu'



class Booking(models.Model):
    first_name = models.CharField(max_length=130)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    def __str__(self):
        return self.first_name



#201 date model demo1
class DateNow(models.Model):
    today_date = models.DateField()
    def __str__(self):
        return self.today_date