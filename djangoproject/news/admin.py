from django.contrib import admin
from .models import Articles

# Регистрация БД для управления ей из панели администратора
admin.site.register(Articles)
