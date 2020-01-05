from django import forms

class EntryForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'placeholder': '',}))
    middle_name = forms.CharField(label='Middle Name', max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': '',}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': '',}))
