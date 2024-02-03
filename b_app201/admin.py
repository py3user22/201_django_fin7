from django.contrib import admin
from .models import DateNow, Booking, Menu


admin.site.register(Menu)

admin.site.register(Booking)

admin.site.register(DateNow)


