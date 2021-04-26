# Файл serializers.py нужен для того, чтобы преобразовывать типы данных python в json

from rest_framework import serializers

from .models import News


class NewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = News  # Модель для сериализации
        fields = ('title', 'category')  # поля для сериализации


class NewsDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = News  # Модель для сериализации
        fields = ('title', 'category', 'created_at', 'updated_at', 'views', 'content',)  # поля для сериализации


class NewsPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'

