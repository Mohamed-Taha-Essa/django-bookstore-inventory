from django.contrib import admin
from .models import Book, Author, Review, Category
# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Author)
