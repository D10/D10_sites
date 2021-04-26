from django.db import models


# Создание СУБД
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)  # строки 6-9: поля БД
    intro = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):  # Магический метод (см. Маг Методы 1 в папке ООП)
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    # Отображение названия таблицы в панели админа в ед.ч и в мн.ч
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
