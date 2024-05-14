from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from .forms import PropertyForm

def property_list(request):
    """Отображает список недвижимости."""
    properties = Property.objects.all()
    paginator = Paginator(properties, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'property/property_list.html', {'properties': properties, 'page_obj': page_obj})

def property_detail(request, pk):
    """Отображает детали конкретной недвижимости."""
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property/property_detail.html', {'property': property})

@user_passes_test(lambda u: u.is_superuser)
def property_create(request):
    """Создает новую недвижимость."""
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property:property_list')
    else:
        form = PropertyForm()
    return render(request, 'property/property_form.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def property_update(request, pk):
    """Редактирует существующую недвижимость."""
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property:property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'property/property_form.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def property_delete(request, pk):
    """Удаляет существующую недвижимость."""
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('property:property_list')
    return render(request, 'property/property_confirm_delete.html', {'property': property})
