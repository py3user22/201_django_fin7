from django import forms
from .models import DateNow, Booking


class MyDateForm(forms.ModelForm):
    model = DateNow
    fields = forms.DateField(input_formats=['%Y/%m/%d'])


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

