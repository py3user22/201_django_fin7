import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import BookingForm
from .models import Booking
from django.http import HttpResponse



def home(request):
    return render(request, '201_forms_demo1.html', {})

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        djo = json.load(request)
        exist = Booking.objects.filter(reservation_date=djo['reservation_date']).filter(reservation_slot=djo['reservation_slot']).exists()

        if exist == False:
            booking = Booking(
                first_name = djo['first_name'],
                reservation_date = djo['reservation_date'],
                reservation_slot = djo['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')

