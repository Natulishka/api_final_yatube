from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename='posts')
router.register('v1/groups', GroupViewSet, basename='groups')
router.register('v1/follow', FollowViewSet, basename='follow')
router.register(r'v1/posts/(?P<post_id>[1-9]\d*)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
