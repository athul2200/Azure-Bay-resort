from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Reservation
from .forms import ReservationForm 


def index_view(request):
    return render(request, "index.html")

def booking_view(request):
    return render(request, 'booking.html')

def page_view(request, page_name):
    if not page_name.endswith('.html'):
        page_name += '.html'
    return render(request, page_name)

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Reservation saved successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    # If accessed via GET, redirect to the booking page
    return redirect('booking')
