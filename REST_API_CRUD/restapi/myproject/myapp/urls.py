from django.contrib import admin
from django.urls import path
# from myapp.views import book_list, book_create, book
from myapp.views import BookCreate, BookList, BookDetail


urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>', BookDetail.as_view())
]