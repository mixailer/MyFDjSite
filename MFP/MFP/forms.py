from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'birth_date', 'phone_number', 'email', 'discount_percentage', 'city']