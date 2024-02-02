import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import BookingForm
from .models import Booking, Menu
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime, date


def home1(request):
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


#0202 adding methods for html pages in templates
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def book(request):
#     form = BookingForm()
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form':form}
#     return render(request, 'book.html', context)

# Add code for the bookings() view



def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})
