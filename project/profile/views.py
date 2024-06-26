from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from client.models import Interaction
from .models import Profile
from .forms import ProfileForm, UserCreateForms


@login_required
def profile_detail(request, pk):
    """Отображает детали профиля."""
    profile = Profile.objects.get(pk=pk)
    interactions = Interaction.objects.filter(profile=profile)
    return render(request, 'profile/profile.html', {'profile': profile, 'interactions': interactions})


@login_required
def profile_update(request, pk):
    """Редактирует профиль пользователя."""
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile:profile', pk=pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/profile_update.html', {'form': form})


def registration(request):
    """Регистрация нового пользователя."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                profile = Profile.objects.create(user=user)
                return redirect('profile:profile', pk=profile.pk)
        else:
            return render(request, 'profile/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'profile/register.html', {'form': form})


@login_required
def profile(request, pk):
    """Отображает профиль пользователя."""
    user_profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profile/profile.html', {'profile': user_profile})


class MyLogoutView(LogoutView):
    """Пользовательское представление выхода из системы."""
    next_page = reverse_lazy("profile:logout")
    http_method_names = ['get', 'post']

    def get_success_url(self):
        return reverse_lazy('profile:login')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile:profile', pk=user.profile.pk)
        else:
            return render(request, 'profile/login.html', {'error_message': 'Неверный логин или пароль'})
    else:
        return render(request, 'profile/login.html')
