from django.urls import path 
from .api import BookList ,BookDetail,AuthoList ,CategoryList
urlpatterns = [
    path('api/book/list' ,BookList.as_view()),
    path('api/book/list/<int:pk>' ,BookDetail.as_view()),

    path('api/author/list' ,AuthoList.as_view()),
    path('api/category/list' ,CategoryList.as_view())
]
