from django import forms
from .models import *

class AddPurch(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = ['title', 'cost', 'buy_date', 'description']
    
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Кофе, Подарок, Проезд',
            'id': 'title'
            }),
        label='Название'
        )
    cost = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'placeholder': '0.00',
            'step': '0.01',
            'min': '0',
            'id': 'cost'
            }),
        label='Сумма (₽)',
        max_digits=10,
        decimal_places=2
    )
    buy_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'id': 'date'
            }),
        label='Дата',
        input_formats=['%Y-%m-%d']
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Короткое описание покупки...',
            'rows': 5,
            'id': 'description'
        }),
        label='Описание',
        required=False
    )
    
    
class AddNote(forms.Form):
    note = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Введите заметку здесь...',
            'rows': 5
        }),
        label='заметка:'
    )