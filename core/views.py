from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from .models import Purchases
from .forms import AddPurch
from django.contrib import messages

from .models import *

# Create your views here.
@login_required
def main(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Для добавления покупок необходимо войти в систему')
            return redirect('login')
        
        form = AddPurch(request.POST)
        if form.is_valid():
            for field_name, field in form.cleaned_data.items():
                if isinstance(field, str):
                    form.cleaned_data[field_name] = field.lower()
            in_title = form.cleaned_data.get('title').lower()
            
            if Purchases.objects.filter(title=in_title, user=request.user).exists():
                form.add_error('title', 'У вас уже есть такая запись')
            else:
                data = form.cleaned_data
                purchases = form.save(commit=False)
                purchases.user = request.user
                purchases.save()
                messages.success(request, 'Покупка успешно добавлена!')
                return redirect('my/')
    else:
        form = AddPurch()

    purchases = Purchases.objects.filter(user=request.user).order_by('-buy_date')
    
    context = {
        'purchases': purchases,
        'form': form,
    }
    return render(request, 'buy/main.html', context)

@login_required
def detail_buy(request, purchase_id):
    purchases = Purchases.objects.get(id=purchase_id)
    context = {
        'purchases': purchases,
    }
    return render(request, 'buy/detail.html', context)

@login_required
def detail_delete(request, purchase_id):
    words = Purchases.objects.get(id=purchase_id)
    words.delete()
    return redirect('/')

@login_required
def detail_edit(request, purchase_id):
    try:
        purchase = Purchases.objects.get(id=purchase_id)
        
        if request.method == 'POST':
            form = AddPurch(request.POST, instance=purchase)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = AddPurch(instance=purchase)
        
        context = {
            'form': form,
            'purchase': purchase,
        }
        return render(request, 'buy/detail_edit.html', context)
        
    except Purchases.DoesNotExist:
        return redirect('/')