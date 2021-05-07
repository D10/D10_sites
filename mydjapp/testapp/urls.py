from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    HomeNews,
    CategoryNews,
    ViewNews,
    CreateNews,
    contact,
    user_login,
    user_logout,
    register,
    ApiNewsListView,
    ApiNewsPost,
    ApiNewsDetailView,
    ReviewCreateView,
    AddStarRatingView,
    ReportersListView
)

urlpatterns = [
    path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('category/<int:category_id>/', CategoryNews.as_view(extra_context={'title': 'Категории'}), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news', CreateNews.as_view(), name='add_news'),
    path('contact/', contact, name='contact'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('apinews/', ApiNewsListView.as_view()),
    path('apinews/<int:pk>/', ApiNewsDetailView.as_view()),
    path('apipost/', ApiNewsPost.as_view()),
    path('review/', ReviewCreateView.as_view()),
    path('rating/', AddStarRatingView.as_view()),
    path('reporters/', ReportersListView.as_view()),
    path('reporters/<int:pk>', ReportersListView.as_view()),
]
