from django import template
from testapp.models import Category, News
from django.db.models import *
from django.core.cache import cache

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('testapp/list_categories.html')
def show_categories():
    news = News.objects.filter(is_published=True)
    categories = cache.get('categoties')
    # categories = Category.objects.filter(pk__in=news)
    if not categories:
        categories = Category.objects.filter(news__is_published=True).distinct()
        cache.set('categories', categories, 30)
    return {"categories": categories}
