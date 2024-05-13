from django import forms
from .models import Contact, Interaction, PropertyRequest, Feedback


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'notes']


class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['description']


class PropertyRequestForm(forms.ModelForm):
    class Meta:
        model = PropertyRequest
        fields = ['user', 'property', 'status']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']
