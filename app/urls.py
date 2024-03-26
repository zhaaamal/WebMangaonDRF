from django.urls import path
from . import views

urlpatterns = [
    # API endpoints for Manga
    path('manga/', views.MangaListCreateAPIView.as_view(), name='manga-list-create'),
    path('manga/<int:pk>/', views.MangaDetailAPIView.as_view(), name='manga-detail'),

    # API endpoints for Comments
    path('comments/', views.CommentCreateAPIView.as_view(), name='comment-create'),
    path('manga/<int:pk>/comments/', views.MangaCommentsAPIView.as_view(), name='manga-comments'),
    path('comments/<int:pk>/', views.CommentDetailAPIView.as_view(), name='comment-detail'),
]
