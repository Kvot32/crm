from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView

from client.models import Interaction
from .models import Profile
from .forms import ProfileForm


@login_required
def profile_detail(request, pk):
    profile = Profile.objects.get(pk=pk)
    interactions = Interaction.objects.filter(profile=profile)
    return render(request, 'profile/profile.html', {'profile': profile, 'interactions': interactions})

@login_required
def profile_update(request, pk):
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
        form = UserCreationForm()
    return render(request, 'profile/register.html', {'form': form})

@login_required
def profile(request, pk):
    user_profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profile/profile.html', {'profile': user_profile})


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("profile:logout")
    http_method_names = ['get', 'post']

    def get_success_url(self):
        return reverse_lazy('profile:login')


class MyLoginView(LoginView):
    template_name = 'profile/login.html'

    def get_success_url(self):
        return reverse_lazy('profile:profile', kwargs={'pk': self.request.user.profile.pk})
