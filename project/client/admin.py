from django.contrib import admin
from .models import Contact, Interaction, PropertyRequest, Feedback

admin.site.register(Contact)
admin.site.register(Interaction)
admin.site.register(PropertyRequest)
admin.site.register(Feedback)
