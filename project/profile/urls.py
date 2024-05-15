from django.urls import path

from .views import user_login, registration, profile_detail, MyLogoutView, profile_update

app_name = 'profile'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', registration, name='register'),
    path('profile/<int:pk>/', profile_detail, name='profile'),
    path('profile_update/<int:pk>/', profile_update, name='profile_update'),
    path('logout/', MyLogoutView.as_view(), name='logout'),


]
