from django import forms

class NewRequest(forms.From):
    name = forms.Charfield(label="Name", max_length=100)
    email = forms.Charfield(label="Email", max_length=100)