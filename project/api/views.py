from rest_framework import generics, viewsets, filters
from rest_framework.permissions import IsAuthenticated

from client.models import Interaction, Contact, Feedback
from .serializers import InteractionSerializer, ContactSerializer, FeedbackSerializer, ProfileSerializer
from profile.models import Profile
from .pagination import CustomPagination


class FeedbackListCreateAPIView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username', 'email']
    pagination_class = CustomPagination