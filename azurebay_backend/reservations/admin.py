from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'resort', 'room_type', 'check_in', 'check_out', 'created_at')
    list_filter = ('resort', 'room_type', 'check_in')
    search_fields = ('name', 'email', 'phone', 'resort')
    date_hierarchy = 'created_at'
