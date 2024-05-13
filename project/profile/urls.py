from django import urls
from django.urls import path

from .views import  MyLoginView, registration, profile_detail, MyLogoutView, profile_update

app_name = 'profile'

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', registration, name='register'),
    path('profile/<int:pk>/', profile_detail, name='profile'),
    path('profile_update/<int:pk>/', profile_update, name='profile_update'),
    path('logout/', MyLogoutView.as_view(), name='logout'),


]
