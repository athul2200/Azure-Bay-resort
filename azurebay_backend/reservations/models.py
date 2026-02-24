from django.db import models

class Reservation(models.Model):
    resort = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.IntegerField()
    children = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.resort} ({self.check_in} to {self.check_out})"
