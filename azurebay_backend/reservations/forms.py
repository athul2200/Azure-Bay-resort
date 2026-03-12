from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['resort', 'room_type', 'check_in', 'check_out', 'adults', 'children', 'name', 'phone', 'email', 'message']

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        resort = cleaned_data.get('resort')
        room_type = cleaned_data.get('room_type')

        if check_in and check_out and resort and room_type:
            if check_in >= check_out:
                raise forms.ValidationError("Check-out date must be after check-in date.")

            # Check for overlapping bookings
            # Logic: (existing_check_in < new_check_out) AND (existing_check_out > new_check_in)
            overlapping_bookings = Reservation.objects.filter(
                resort=resort,
                room_type=room_type,
                check_in__lt=check_out,
                check_out__gt=check_in
            )

            if overlapping_bookings.exists():
                raise forms.ValidationError(
                    "This room is already booked for the selected dates. Please choose different dates or another room."
                )

        return cleaned_data
