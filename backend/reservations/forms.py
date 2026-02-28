from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['resort', 'room_type', 'check_in', 'check_out', 'adults', 'children', 'name', 'phone', 'email', 'message']
