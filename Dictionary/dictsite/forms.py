from django import forms
from .models import Translations
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginFrom(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(max_length=150, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password1 = forms.CharField(max_length=150, label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=150, label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'rows': 5}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }


class TranslationsForm(forms.ModelForm):
    class Meta:
        model = Translations
        fields = ['term', 'translation', 'another_translations', 'definition']
        widgets = {
            'term': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'translation': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'value': 'TestTest'}),
            'another_translations': forms.TextInput(attrs={'class': 'form-control',
                                                           'autocomplete': 'off', 'value': 'TestTest'}),
            'definition': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'autocomplete': 'off'})
        }
