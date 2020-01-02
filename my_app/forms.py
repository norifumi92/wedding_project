from django import forms

class EntryForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)