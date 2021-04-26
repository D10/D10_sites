
from django.urls import path
from django.views.decorators.cache import cache_page
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', cache_page(10)(HomeView.as_view()), name='home'),
    path('add_term/', TermAdd.as_view(), name='add_term'),
    path('login/', user_login, name='login'),
    path('admin_panel/', AdminPanel.as_view(), name='admin_panel'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('terms_db/', TermsDB.as_view(), name='terms_db')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
