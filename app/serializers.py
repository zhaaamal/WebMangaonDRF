from rest_framework import serializers
from .models import Manga, Comment, Author, Category, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MangaSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    genre = GenreSerializer()
    total_comments = serializers.SerializerMethodField()

    def get_total_comments(self, obj):
        return obj.comments.count()

    class Meta:
        model = Manga
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    def validate_content(self, value):
        """
        Проверяет, что содержание комментария не содержит нецензурную лексику.
        """
        bad_words = ['suka', 'blyat']  # список запрещенных слов
        for word in bad_words:
            if word in value:
                raise serializers.ValidationError("Комментарий содержит недопустимое слово.")
        return value

    class Meta:
        model = Comment
        fields = '__all__'
