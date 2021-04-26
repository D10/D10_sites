from django.shortcuts import render, redirect, HttpResponse
from .models import Translations
from .forms import *
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib import messages  # Сообщения об успехе/ошибке регистрации


class HomeView(ListView):
    model = Translations
    template_name = 'dictsite/index.html'
    context_object_name = 'translations'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        if query == '':
            object_list = 0
        elif query:
            object_list = Translations.objects.filter(term__icontains=query)
        else:
            object_list = Translations.objects.all()
        return object_list


def home(request):
    search_querry = request.GET.get('search', '')
    if search_querry:
        translations = Translations.objects.filter(term__icontains=search_querry)
    else:
        translations = 0

    return render(request, 'dictsite/index.html', {'translations': translations})


class TermAdd(LoginRequiredMixin, CreateView):
    form_class = TranslationsForm
    template_name = 'dictsite/terms_add.html'
    success_url = reverse_lazy('add_term')
    raise_exception = True


class AdminPanel(LoginRequiredMixin, ListView):
    model = Translations
    template_name = 'dictsite/admin_panel.html'
    raise_exception = True


def register(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'Вы успешно зарегестрировались!')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка регистрации!')
        else:
            form = UserRegisterForm
        return render(request, 'dictsite/register.html', {'form': form})
    else:
        return redirect('home')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginFrom(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_panel')
    else:
        form = UserLoginFrom()
    return render(request, 'dictsite/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


class TermsDB(LoginRequiredMixin, ListView):
    model = Translations
    template_name = 'dictsite/terms_db.html'
    context_object_name = 'terms'
    raise_exception = True
    paginate_by = 7

    def get_queryset(self):
        query = self.request.GET.get('db_search', '')
        if query == 'all':
            object_list = Translations.objects.order_by('id')
        elif query:
            object_list = Translations.objects.filter(term__icontains=query)
        else:
            object_list = Translations.objects.all()
        return object_list
