from django.shortcuts import render
from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import User, Genre, Category, Title, Review, Comment

from .serializers import (
    UserSerializer,
    GenreSerializer,
    CategorySerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = LimitOffsetPagination