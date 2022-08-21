from django.contrib import admin
from django.urls import path
from myapp.views import SchoolList, SchoolCreate, SchoolDetail

urlpatterns = [
    path('', SchoolCreate.as_view()),
    path('list/', SchoolList.as_view()),
    path('<int:pk>', SchoolDetail.as_view()),
]
