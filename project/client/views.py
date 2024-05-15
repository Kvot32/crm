from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Interaction
from .forms import InteractionForm, PropertyRequestForm, FeedbackForm
from profile.models import Profile


@user_passes_test(lambda u: u.is_superuser)
def interaction_list(request):
    """
    Возвращает список всех заявок.
    """
    interactions = Interaction.objects.select_related('profile', 'contact').all()
    paginator = Paginator(interactions, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'client/interaction_list.html', {'interactions': interactions, 'page_obj': page_obj})


@user_passes_test(lambda u: u.is_superuser)
def interaction_detail(request, pk):
    """
    Возвращает детали конкретного заявок.
    """
    interaction = get_object_or_404(Interaction, pk=pk)
    return render(request, 'client/interaction_detail.html', {'interaction': interaction})


@user_passes_test(lambda u: u.is_superuser)
def contact_list(request):
    """
    Возвращает список контактов и профилей.
    """
    contacts = Contact.objects.all()
    profiles = Profile.objects.all()
    combined_list = list(contacts) + list(profiles)
    paginator = Paginator(combined_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'client/contact_list.html',
                  {'contacts': contacts, 'profiles': profiles, 'page_obj': page_obj})


@user_passes_test(lambda u: u.is_superuser)
def contact_detail(request, pk):
    """
    Возвращает детали конкретного контакта.
    """
    contact = Contact.objects.get(pk=pk)
    interactions = Interaction.objects.filter(contact=contact)
    return render(request, 'client/contact_detail.html', {'contact': contact, 'interactions': interactions})


def create_interaction(request):
    """
    Создает новую заявку и сохраняет ее в базе данных.
    """
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            if request.user.profile:
                interaction.profile = request.user.profile
            elif request.user.contacts.exists():
                interaction.contact = request.user.contacts.first()
            interaction.save()
            if interaction.profile:
                return redirect('profile:profile', pk=interaction.profile.pk)
            elif interaction.contact:
                return redirect('client:interaction_list')
            else:
                return redirect('property:property_list')
    else:
        form = InteractionForm()
    return render(request, 'client/interaction_form.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def property_request_create(request, property_id):
    """
    Создает новый запрос на просмотр объекта недвижимости и сохраняет его в базе данных.
    """
    if request.method == 'POST':
        form = PropertyRequestForm(request.POST)
        if form.is_valid():
            property_request = form.save(commit=False)
            property_request.user = request.user
            property_request.property_id = property_id
            property_request.save()
            return redirect('property:property_detail', pk=property_id)
    else:
        form = PropertyRequestForm()
    return render(request, 'client/property_request_form.html', {'form': form})


def feedback_create(request):
    """
    Создает новый отзыв и сохраняет его в базе данных.
    """
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('client:interactions')
    else:
        form = FeedbackForm()
    return render(request, 'client/feedback_form.html', {'form': form})
