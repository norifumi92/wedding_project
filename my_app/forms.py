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

COUNTRY_OPTIONS= [
    ('', ''),
    ('Japan', 'Japan'),
    ('The United Sates', 'The United Sates'),
    ('Malaysia', 'Malaysia'),
    ('India', 'India'),
    ('China', 'China'),
    ('The Philippines', 'The Philippines'),
    ('Indonesia', 'Indonesia'),
    ('France', 'France'),
    ('Poland', 'Poland'),
    ('Laos', 'Laos'),
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
            'first_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'gender': forms.Select(choices=GENDER_OPTIONS),
            'nationality': forms.Select(choices=COUNTRY_OPTIONS),
            'meal_preference': forms.Select(choices=COUNTRY_OPTIONS)
        }
        labels = {
            'phone_number': 'Phone Number (Whatsapp)',
        }
