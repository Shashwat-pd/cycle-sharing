from location_field.forms.plain import PlainLocationField
from django import forms
from .models import Order

class MyForm(forms.ModelForm):
    location = PlainLocationField()
    class Meta:
        model = Order
        fields = ('starting_point',)
