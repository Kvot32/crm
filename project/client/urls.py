from django.urls import path
from .views import contact_list, contact_detail, create_interaction, property_request_create, feedback_create, interaction_list, interaction_detail

app_name = 'client'

urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('create_interaction/', create_interaction, name='create_interaction'),
    path('interactions/', interaction_list, name='interactions'),
    path('interaction/<int:pk>/', interaction_detail, name='interaction_detail'),
    path('property/request/<int:property_id>/', property_request_create, name='property_request_create'),
    path('feedback/', feedback_create, name='feedback_create'),
]
