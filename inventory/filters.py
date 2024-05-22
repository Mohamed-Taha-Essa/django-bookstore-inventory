from django_filters import rest_framework as filters
from .models import Book


class BookFilter(filters.FilterSet):
    in_stock = filters.BooleanFilter(method='filter_in_stock')

    class Meta:
        model = Book
        fields = ['category', 'author', 'price', 'quantity']

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(quantity__gt=0)
        else:
            return queryset.filter(quantity=0)
