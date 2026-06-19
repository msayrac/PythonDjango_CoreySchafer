from django.urls import path
from blog.api import views as api_views
from blog.api.views import PostListCreateAPIView, PostDetailAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='api-post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='api-post-detail'),
]