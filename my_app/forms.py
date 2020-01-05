from django import forms

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
    ('France', 'France'),
    ('Poland', 'Poland'),
    ('Laos', 'Laos'),
    ]

MEAL_OPTIONS= [
    ('None', 'None'),
    ('Vegitarian', 'Vegitarian'),
]

class EntryForm(forms.Form):

    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'placeholder': '',}))
    middle_name = forms.CharField(label='Middle Name', max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': '',}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': '',}))
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(label='Phone Number (Whatsapp)',max_length=15)
    Gender = forms.CharField(required=True, widget=forms.Select(choices=GENDER_OPTIONS))
    nationality = forms.CharField(widget=forms.Select(choices=COUNTRY_OPTIONS))
    meal_preference = forms.CharField(widget=forms.Select(choices=MEAL_OPTIONS))