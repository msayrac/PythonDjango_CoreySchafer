from django.urls import path
from blog.api import views as api_views

urlpatterns = [
    path('posts/', api_views.PostListCreateAPIView.as_view(), name='api-post-list')
]