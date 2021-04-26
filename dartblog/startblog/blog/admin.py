from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django import forms


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id', 'title', 'slug']
    save_on_top = True


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['id', 'title', 'slug', 'created_at', 'views', 'photo']
    list_display_links = ['id', 'title']
    list_filter = ['category', 'tags']
    save_as = True  # Добавляет кнопку "Сохранить как новый объект" в админке
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'фото'


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id', 'title', 'slug']

    save_on_top = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
