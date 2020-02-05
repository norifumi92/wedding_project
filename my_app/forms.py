from django import forms
#add ModelForm
from django.forms import ModelForm

#import Model
from my_app.models import Attendee

GENDER_OPTIONS= [
    ('', ''),
    ('Male', 'Male'),
    ('Female', 'Female'),
]

#Space is not allowed or ValueError would occur.
COUNTRY_OPTIONS= [
    ('', ''),
    ('Japanese', 'Japanese'),
    ('Korean', 'Korean'),
    ('American', 'American'),
    ('Malaysian', 'Malaysian'),
    ('Indian', 'Indian'),
    ('Chinese', 'Chinese'),
    ('Filipino', 'Filipino'),
    ('Indonesian', 'Indonesian'),
    ('French', 'French'),
    ('Polish', 'Polish'),
    ('Lao', 'Lao'),
    ]

MEAL_OPTIONS= [
    ('None', 'None'),
    ('Vegetarian', 'Vegetarian'),
]

class AttendeeModelForm(ModelForm):
    class Meta:
        model = Attendee
        #select fields to be used
        fields = '__all__'
        widgets = {
            'event': forms.HiddenInput(),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Start from + Country Code'}),
            'gender': forms.Select(choices=GENDER_OPTIONS),
            'nationality': forms.Select(choices=COUNTRY_OPTIONS),
            'meal_preference': forms.Select(choices=MEAL_OPTIONS)
        }
        labels = {
            'phone_number': 'Phone Number (Whatsapp)',
        }
