from django import forms
from .models import Purchases

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title:
            return title.strip()
        return title
    
    def clean_cost(self):
        cost = self.cleaned_data.get('cost')
        if cost is not None and cost < 0:
            raise forms.ValidationError("Стоимость не может быть отрицательной")
        return cost
    
    
class AddNote(forms.Form):
    note = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Введите заметку здесь...',
            'rows': 5,
            'class': 'form-control'
        }),
        label='Заметка:'
    )
    
    def clean_note(self):
        note = self.cleaned_data.get('note')
        if note:
            return note.strip()
        return note