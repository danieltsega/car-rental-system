from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    MANUAL = 'M'
    AUTOMATIC = 'A'
    GEARBOX_CHOICES = [(MANUAL, 'Manual'), (AUTOMATIC, 'Automatic')]
    
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    availabile = models.BooleanField(default=True)
    seat = models.PositiveIntegerField()
    door = models.PositiveIntegerField()
    gearbox = models.CharField(max_length=1, choices=GEARBOX_CHOICES)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} ({self.model})"

class Customer(models.Model):
    phone_number = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}'s Customer Profile"

class Booking(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    car = models.OneToOneField(Car, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Booking ID: {self.id} - {self.car.name} ({self.start_date} to {self.end_date})"
    
    def clean(self):
        # Check for overlapping bookings for the same car
        overlapping_bookings = Booking.objects.filter(
            car=self.car,
            end_date__gte=self.start_date,
            start_date__lte=self.end_date
        ).exclude(pk=self.pk)  # Exclude the current booking if it's an update
        if overlapping_bookings.exists():
            raise ValidationError("This car is already booked for the specified time period.")

    def save(self, *args, **kwargs):
        self.clean()  # Perform the validation before saving
        super().save(*args, **kwargs)
    
class Review(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    
    def __str__(self):
        return f"Review ID: {self.id} - {self.name} on {self.car.name}"
