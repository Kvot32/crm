from django.urls import path, include

from .views import FeedbackListCreateAPIView, InteractionViewSet, ProfileViewSet, ContactViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('interaction', InteractionViewSet, basename='interactions')
router.register('profile', ProfileViewSet, basename='profiles')
router.register('contact', ContactViewSet, basename='contacts')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('feedbacks/', FeedbackListCreateAPIView.as_view(), name='feedback_api'),
]
