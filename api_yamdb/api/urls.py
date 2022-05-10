from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    GenreViewSet,
    CategoryViewSet,
    TitleViewSet,
)


router = DefaultRouter()
router.register("genres", GenreViewSet, basename='genres')
router.register("categories", CategoryViewSet, basename='categories')
router.register("titles", TitleViewSet, basename='titles')
router.register(
    r"^titles/(?P<title_id>\d+)/",
    TitleViewSet, basename="title"
)


urlpatterns = [
    path("v1/", include(router.urls)),
]
