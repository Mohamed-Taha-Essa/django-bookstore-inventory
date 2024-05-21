from rest_framework import generics
from . serializers import BookDetailSerializer , BookListSerializer

from .models import Book ,Author ,Review ,Category


class BookList(generics.ListAPIView):
    queryset =Book.objects.all()
    serializer_class =BookListSerializer
    

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer