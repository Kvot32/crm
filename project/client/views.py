from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Interaction
from .forms import InteractionForm, PropertyRequestForm, FeedbackForm
from profile.models import Profile


@user_passes_test(lambda u: u.is_superuser)
def interaction_list(request):
    interactions = Interaction.objects.select_related('profile', 'contact').all()
    return render(request, 'client/interaction_list.html', {'interactions': interactions})


@user_passes_test(lambda u: u.is_authenticated)
def interaction_detail(request, pk):
    interaction = get_object_or_404(Interaction, pk=pk)
    return render(request, 'client/interaction_detail.html', {'interaction': interaction})


@user_passes_test(lambda u: u.is_superuser)
def contact_list(request):
    contacts = Contact.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'client/contact_list.html', {'contacts': contacts, 'profiles': profiles})


@user_passes_test(lambda u: u.is_superuser)
def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    interactions = Interaction.objects.filter(contact=contact)
    return render(request, 'client/contact_detail.html', {'contact': contact, 'interactions': interactions})


# Представления для управления заявками

def create_interaction(request):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            # Сохраняем данные из формы в объект Interaction
            interaction = form.save(commit=False)
            # Устанавливаем профиль или контакт в зависимости от пользователя
            if request.user.profile:
                interaction.profile = request.user.profile
            elif request.user.contacts.exists():
                interaction.contact = request.user.contacts.first()
            # Сохраняем объект Interaction в базу данных
            interaction.save()
            # После успешного сохранения перенаправляем пользователя
            # на соответствующую страницу
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
# Представления для управления запросами на просмотр объектов
def property_request_create(request, property_id):
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


@user_passes_test(lambda u: u.is_authenticated)
# Представление для управления обратной связью
def feedback_create(request):
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
