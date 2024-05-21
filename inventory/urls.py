from django.urls import path 
from .api import BookList ,BookDetail
urlpatterns = [
    path('api/list' ,BookList.as_view()),
    path('api/list/<int:pk>' ,BookDetail.as_view())
]
