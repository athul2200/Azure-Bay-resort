from django.test import TestCase
from django.utils import timezone
from .models import Reservation
from .forms import ReservationForm
import datetime

class ReservationValidationTest(TestCase):
    def setUp(self):
        # Create an existing reservation
        self.existing_res = Reservation.objects.create(
            resort="Munnar",
            room_type="MOUNTAIN VIEW COTTAGE",
            check_in=datetime.date(2026, 4, 10),
            check_out=datetime.date(2026, 4, 15),
            adults=2,
            children=0,
            name="Existing Guest",
            phone="1234567890",
            email="existing@example.com"
        )

    def test_no_overlap_before(self):
        """No overlap: New booking ends before existing booking starts."""
        data = {
            'resort': 'Munnar',
            'room_type': 'MOUNTAIN VIEW COTTAGE',
            'check_in': '2026-04-01',
            'check_out': '2026-04-05',
            'adults': 1,
            'children': 0,
            'name': 'New Guest',
            'phone': '0987654321',
            'email': 'new@example.com'
        }
        form = ReservationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_no_overlap_after(self):
        """No overlap: New booking starts after existing booking ends."""
        data = {
            'resort': 'Munnar',
            'room_type': 'MOUNTAIN VIEW COTTAGE',
            'check_in': '2026-04-20',
            'check_out': '2026-04-25',
            'adults': 1,
            'children': 0,
            'name': 'New Guest',
            'phone': '0987654321',
            'email': 'new@example.com'
        }
        form = ReservationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_same_dates_overlap(self):
        """Overlap: Same check-in and check-out dates."""
        data = {
            'resort': 'Munnar',
            'room_type': 'MOUNTAIN VIEW COTTAGE',
            'check_in': '2026-04-10',
            'check_out': '2026-04-15',
            'adults': 1,
            'children': 0,
            'name': 'New Guest',
            'phone': '0987654321',
            'email': 'new@example.com'
        }
        form = ReservationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("This room is already booked", form.errors['__all__'][0])

    def test_start_overlap(self):
        """Overlap: New check-in date falling within an existing booking period."""
        data = {
            'resort': 'Munnar',
            'room_type': 'MOUNTAIN VIEW COTTAGE',
            'check_in': '2026-04-12',
            'check_out': '2026-04-18',
            'adults': 1,
            'children': 0,
            'name': 'New Guest',
            'phone': '0987654321',
            'email': 'new@example.com'
        }
        form = ReservationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("This room is already booked", form.errors['__all__'][0])

    def test_end_overlap(self):
        """Overlap: New check-out date falling within an existing booking period."""
        data = {
            'resort': 'Munnar',
            'room_type': 'MOUNTAIN VIEW COTTAGE',
            'check_in': '2026-04-05',
            'check_out': '2026-04-12',
            'adults': 1,
            'children': 0,
            'name': 'New Guest',
            'phone': '0987654321',
            'email': 'new@example.com'
        }
        form = ReservationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("This room is already booked", form.errors['__all__'][0])

    def test_completely_covering_overlap(self):
        """Overlap: New booking completely covering an existing booking period."""
        data = {
            'resort': 'Munnar',
            'room_type': 'MOUNTAIN VIEW COTTAGE',
            'check_in': '2026-04-05',
            'check_out': '2026-04-20',
            'adults': 1,
            'children': 0,
            'name': 'New Guest',
            'phone': '0987654321',
            'email': 'new@example.com'
        }
        form = ReservationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("This room is already booked", form.errors['__all__'][0])

    def test_existing_covers_new_overlap(self):
        """Overlap: Existing booking completely covering the new booking period."""
        data = {
            'resort': 'Munnar',
            'room_type': 'MOUNTAIN VIEW COTTAGE',
            'check_in': '2026-04-11',
            'check_out': '2026-04-14',
            'adults': 1,
            'children': 0,
            'name': 'New Guest',
            'phone': '0987654321',
            'email': 'new@example.com'
        }
        form = ReservationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("This room is already booked", form.errors['__all__'][0])

    def test_back_to_back_no_overlap_start(self):
        """No Overlap: New booking ends on existing check-in day."""
        data = {
            'resort': 'Munnar',
            'room_type': 'MOUNTAIN VIEW COTTAGE',
            'check_in': '2026-04-05',
            'check_out': '2026-04-10',
            'adults': 1,
            'children': 0,
            'name': 'New Guest',
            'phone': '0987654321',
            'email': 'new@example.com'
        }
        form = ReservationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_back_to_back_no_overlap_end(self):
        """No Overlap: New booking starts on existing check-out day."""
        data = {
            'resort': 'Munnar',
            'room_type': 'MOUNTAIN VIEW COTTAGE',
            'check_in': '2026-04-15',
            'check_out': '2026-04-20',
            'adults': 1,
            'children': 0,
            'name': 'New Guest',
            'phone': '0987654321',
            'email': 'new@example.com'
        }
        form = ReservationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_different_room_no_overlap(self):
        """No Overlap: Same dates but different room type."""
        data = {
            'resort': 'Munnar',
            'room_type': 'HONEYMOON COTTAGE',
            'check_in': '2026-04-10',
            'check_out': '2026-04-15',
            'adults': 1,
            'children': 0,
            'name': 'New Guest',
            'phone': '0987654321',
            'email': 'new@example.com'
        }
        form = ReservationForm(data=data)
        self.assertTrue(form.is_valid())
