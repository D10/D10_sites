from django.contrib import admin
from .models import News, Category, Reviews, Rating, RatingStar
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)  # позволяет редактировать поле таблицы, не открывая ее
    list_filter = ('is_published', 'category')  # позволяет фильтровать данные таблицы по этим полям
    fields = ('title', 'category', 'content', 'photo', 'get_photo',
              'is_published', 'views', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75"')
        else:
            return 'Фото не установлено'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "news")


class RatingStarsAdmin(admin.ModelAdmin):
    list_display = ("id", "value")


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reviews)
admin.site.register(Rating)
admin.site.register(RatingStar, RatingStarsAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
