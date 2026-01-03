from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
   
    path('', include(router.urls)),
    
    path('feed/', FeedView.as_view({'get': 'list'}), name='user-feed'),
    
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
]
