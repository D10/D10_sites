# Файл serializers.py нужен для того, чтобы преобразовывать типы данных python в json

from rest_framework import serializers

from .models import News, Reporter, Reviews, Rating


class FilterReviewSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class NewsListSerializer(serializers.ModelSerializer):
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = News  # Модель для сериализации
        fields = ("id", 'title', 'category', 'rating_user', 'middle_star')  # поля для сериализации


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)  # Для вывода отзывов в виде дерева

    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Reviews
        fields = ('name', 'text', 'children')


class ReporterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = "__all__"


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = ("id", "name", "image")


class NewsDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    reviews = ReviewSerializer(many=True)
    reporters = ReporterSerializer(read_only=True, many=True)

    class Meta:
        model = News  # Модель для сериализации
        fields = ('title', 'category', 'created_at', 'updated_at',
                  'views', 'content', 'reviews', 'reporters')  # поля для сериализации


class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


# Возможность оставлять отзывы и ставить звезды (привязка ip)
class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("star", "news")

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            news=validated_data.get('news', None),
            defaults={"star": validated_data.get("star")}
        )

        return rating
