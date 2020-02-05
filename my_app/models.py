from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Attendee(models.Model):
    #Add Validator here
    nationality_regex = RegexValidator(regex=r'^[a-zA-Z0-9_ ]*$', message = ("Error."))
    
    #Define fields
    event = models.CharField(max_length=15, blank=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    nationality = models.CharField(validators=[nationality_regex],max_length=15)
    meal_preference = models.CharField(max_length=15)
    comment = models.TextField(blank=True)