from .models import Articles
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import DateTimeInput
from django.forms import Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles  # БД, с которой мы работаем
        fields = ['title', 'intro', 'full_text', 'date']  # Поля БД

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "intro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }
