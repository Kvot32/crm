from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Interaction(models.Model):
    number = models.AutoField(primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='interactions', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    profile = models.ForeignKey('profile.Profile', on_delete=models.CASCADE, related_name='interactions', blank=True, null=True)

    def __str__(self):
        if self.contact:
            return f"{self.number} - {self.contact} - {self.date}"
        else:
            return f"{self.number} - {self.profile} - {self.date}"


class PropertyRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property_requests')
    property = models.ForeignKey('property.Property', on_delete=models.CASCADE, related_name='property_requests')
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.user} - {self.property}"


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.date}"
