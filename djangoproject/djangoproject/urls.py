from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Здесь прописываются URl адреса для страниц сайта
urlpatterns = [
                  path('admin/', admin.site.urls),  # Панель администратора
                  path('', include('main.urls')),   # Главная страница
                  path('news/', include('news.urls'))   # Страница с новостями
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''                                ^
                                   |
    -------------------------------
    |
    Вспомогательная функция, которая
    обслуживает файлы из STATIC_ROOT
'''
