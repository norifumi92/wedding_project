from django.db import models

# Create your models here.
class Attendee(models.Model):
    event = models.CharField(max_length=15, blank=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    nationality = models.CharField(max_length=15)
    meal_preference = models.CharField(max_length=15)
    comment = models.TextField(blank=True)