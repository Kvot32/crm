from rest_framework import serializers
from django.core.validators import EmailValidator
from client.models import Interaction, Contact, Feedback
from profile.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = 'id', 'first_name', 'last_name', 'email', 'phone'

class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    class Meta:
        model = Contact
        fields = 'id', 'user', 'name', 'email', 'phone', 'notes'

class InteractionSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = Interaction
        fields = 'date', 'description', 'profile', 'contact'
        read_only_fields = ('id',)

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = 'id', 'user', 'date', 'message'
        read_only_fields = ('id',)