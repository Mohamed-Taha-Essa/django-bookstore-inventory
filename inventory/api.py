from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from . serializers import BookDetailSerializer , BookListSerializer,AuthorSerializer,CategorySerializer
from .filters import BookFilter
from .models import Book ,Author ,Review ,Category



class BookList(generics.ListCreateAPIView):
    queryset =Book.objects.all()

    serializer_class =BookListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class =BookFilter



class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class AuthoList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class =AuthorSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer