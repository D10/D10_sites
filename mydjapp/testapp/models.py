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
    reporters = models.ManyToManyField('Reporter', verbose_name='Репортеры', related_name='reporters')
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
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL,
                               blank=True, null=True, related_name='children')
    news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.name} - {self.news}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="новость", related_name='ratings')

    def __str__(self):
        return f"{self.star} - {self.news}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reporter(models.Model):
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Репортер"
        verbose_name_plural = "Репортеры"
