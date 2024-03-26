from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)  # Renamed from status
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='manga_images/')  # Added upload_to for ImageField

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.manga.title}'

