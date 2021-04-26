from django.db import models


class Translations(models.Model):
    term = models.CharField(max_length=150, verbose_name='Термин')
    translation = models.CharField(max_length=150, verbose_name='Перевод')
    another_translations = models.CharField(max_length=150, verbose_name='Другие варианты перевода')
    definition = models.TextField(blank=True, verbose_name='Значение')

    def __str__(self):
        return self.term

    class Meta:
        verbose_name = 'Термин'
        verbose_name_plural = 'Термины'
