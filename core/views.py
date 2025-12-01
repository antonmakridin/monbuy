from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Purchases
from .forms import AddPurch
from django.contrib import messages

from .models import *

# Create your views here.
def main(request):
    if request.method == 'POST':
        form = AddPurch(request.POST)
        if form.is_valid():
            for field_name, field in form.cleaned_data.items():
                if isinstance(field, str):
                    form.cleaned_data[field_name] = field.lower()
            in_title = form.cleaned_data.get('title').lower()
            if Purchases.objects.filter(title=in_title).exists():
                form.add_error('title', 'Уже есть такая запись')
            else:
                data = form.cleaned_data
                purchases = Purchases.objects.create(**data)
                return redirect('/')
    else:
        form = AddPurch()

    purchases = Purchases.objects.all()
    context = {
        'purchases': purchases,
        'form': form,
    }
    return render(request, 'buy/main.html', context)

def detail_buy(request, purchase_id):
    purchases = Purchases.objects.get(id=purchase_id)
    context = {
        'purchases': purchases,
    }
    return render(request, 'buy/detail.html', context)

def detail_delete(request, purchase_id):
    words = Purchases.objects.get(id=purchase_id)
    words.delete()
    return redirect('/')


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