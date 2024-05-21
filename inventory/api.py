from rest_framework import generics
from . serializers import BookDetailSerializer , BookListSerializer,AuthorSerializer,CategorySerializer

from .models import Book ,Author ,Review ,Category


class BookList(generics.ListCreateAPIView):
    queryset =Book.objects.all()
    serializer_class =BookListSerializer
    

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class AuthoList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class =AuthorSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer