from django.shortcuts import render, redirect
from .forms import DealForm
from client.models import Contact
from profile.models import Profile
from .models import Deal

def created_deal(request):
    if request.method == 'POST':
        form = DealForm(request.POST, request.FILES)
        if form.is_valid():
            deal = form.save(commit=False)
            client = request.POST.get('client_id')
            if client:
                deal.client = Contact.objects.get(user_id=client)
            profile_id = request.POST.get('profile_id')
            if profile_id:
                deal.assigned_to = Profile.objects.get(id=profile_id)
            deal.save()
            return redirect('deal:deals')
        else:
            return redirect('deal:deal_create')
    else:
        form = DealForm()
        return render(request, 'deal/deal_create.html', {'form':form})


def deal_list(request):
    deals = Deal.objects.all().select_related('client', 'assigned_to')
    return render(request, 'deal/deals.html', {'deals':deals})