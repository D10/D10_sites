from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(blank=True,
                               verbose_name='Контент')  # blank означает, что данное поле необязательно для заполнения
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='https://picsum.photos/200', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация в ленте')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'  # ед.ч
        verbose_name_plural = 'Новости'  # мн.ч
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=150,
                             db_index=True,
                             verbose_name='Категория')
    # db_index устанавливает индекс для поля, что ускоряет поиск внутри поля

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['pk']


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.name} - {self.news}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
