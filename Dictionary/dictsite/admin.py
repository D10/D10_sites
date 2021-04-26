from django.contrib import admin
from .models import Translations


class TranslationsAdmin(admin.ModelAdmin):
    list_display = ("id", "term", "translation", "another_translations", "definition")
    list_display_links = ("id", "term")
    list_filter = ("term",)
    fields = ("term", "translation", "another_translations", "definition")
    save_on_top = True


admin.site.register(Translations, TranslationsAdmin)

admin.site.site_title = "Администрирование MeDictionary"
admin.site.site_header = "Администрирование MeDictionary"
