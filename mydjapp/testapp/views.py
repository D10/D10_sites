from django.shortcuts import render, redirect  # для рендера страниц в ф-ях
from django.views.generic import ListView, DetailView, CreateView  # для рендера страниц в ООП
from django.urls import reverse_lazy  # "Ленивая" загрузка для оптимизации
from django.contrib.auth.mixins import LoginRequiredMixin  # Импортированный миксин для формы добавления
from django.core.paginator import Paginator  # Для постраничной навигации
from django.contrib.auth.forms import UserCreationForm  # Форма для регистрации пользователей
from django.contrib import messages  # Сообщения об успехе/ошибке регистрации
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView  # Главный класс DRF, основан на Django view

from .models import News, Category  # Наши БД
from .forms import NewsForm, UserRegisterForm, UserLoginForm, UserContactForm  # Форма для добавления новостей
from .utils import MyMixin  # Просто созданный мной миксин
from .serializers import NewsListSerializer, NewsDetailSerializer, NewsPostSerializer


class ApiNewsListView(APIView):

    def get(self, request):  # Данная функция будет срабатывать при get запросе
        news = News.objects.filter(is_published=True)
        serializer = NewsListSerializer(news, many=True)  # many=True говорит о том, что у нас будет несколько записей
        return Response(serializer.data)


class ApiNewsDetailView(APIView):

    def get(self, request, pk):
        news = News.objects.get(id=pk, is_published=True)
        serializer = NewsDetailSerializer(news)
        return Response(serializer.data)


class ApiNewsPost(APIView):

    def post(self, request):
        posts = NewsPostSerializer(data=request.data)
        if posts.is_valid():
            posts.save()
        return Response(status=201)


class HomeNews(MyMixin, ListView):
    paginate_by = 5
    model = News
    template_name = 'testapp/news_list.html'
    context_object_name = 'news'
    extra_context = {'title': 'Главная'}
    mixin_prop = 'hello world'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class CategoryNews(MyMixin, ListView):
    paginate_by = 5
    model = News
    context_object_name = 'news'
    extra_context = {'title'}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    template_name = 'testapp/news_detail.html'
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'testapp/add_news.html'
    success_url = reverse_lazy('add_news')
    raise_exception = True


def contact(request):
    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                             'bogdan1414let@gmail.com', ['rgadamurov@bk.ru'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = UserContactForm()
    return render(request, 'testapp/test.html', {'form': form})


def register(request):
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
    return render(request, 'testapp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'testapp/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

# def index(request):
#     news = News.objects.order_by('-created_at')
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'testapp/_index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'testapp/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'testapp/_view_news.html', {'news_item': news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'testapp/add_news.html', {'form': form})
