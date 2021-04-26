# Файл приложения main, в котором обозначены url адреса всех страниц этого веб приложения
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about')
]