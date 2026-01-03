from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView
from .views import like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls

urlpatterns += [
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
]
