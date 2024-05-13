from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['address', 'property_type', 'bedrooms', 'bathrooms', 'area', 'price', 'description', 'photo']
