from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

app_name = "api"
router = DefaultRouter()

router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
router.register("follow", FollowViewSet, basename="followers")
router.register(
    r"posts/(?P<post_id>[\d.]+)/comments",
    CommentViewSet,
    basename="comments",
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
