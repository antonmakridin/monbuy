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

    # purchases = Purchases.objects.all().filter(is_active=False)
    purchases = Purchases.objects.all()
    context = {
        'purchases': purchases,
        'form': form,
    }
    return render(request, 'buy/main.html', context)

# def word(request):
#     if request.method == 'POST':
#         form = AddNote(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             note = Note.objects.create(**data)
#             return redirect('/word/')
#     else:
#         form = AddNote()
#     notes = Note.objects.all()
#     words = Words.objects.all().filter(is_active=True)
#     context = {
#         'words': words,
#         'form': form,
#         'notes': notes,
#     }
#     return render(request, 'word/word_success.html', context)

# def show_word(request, word_id):
#     words = Words.objects.get(id=word_id)
#     context = {
#         'words': words,
#     }
#     return render(request, 'word/word.html', context)

# def delete_word(request, word_id):
#     words = Words.objects.get(id=word_id)
#     words.delete()
#     return redirect('/')


# def learn_word(request, word_id):
#     word = get_object_or_404(Words, id=word_id)
#     word.is_active = True
#     word.save()
#     messages.success(request, f'Слово "{word.slovo}" отмечено как изученное')
#     return redirect('/')