from django_filters.rest_framework import FilterSet, filters
from client.models import Contact

class ContactFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')

    class Meta:
        model = Contact
        fields = ['name', 'email']