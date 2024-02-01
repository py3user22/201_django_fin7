from django.contrib import admin
from .models import Solar, DateNow, Booking


admin.site.register(Solar)

admin.site.register(Booking)

admin.site.register(DateNow)


