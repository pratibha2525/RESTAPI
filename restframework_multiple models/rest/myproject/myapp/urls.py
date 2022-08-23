from django.contrib import admin
from django.urls import path
from myapp.views import empmodels1API,EmpCreate,empDetail,cricketmodels2API,cricketCreate,cricketDetail

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', EmpCreate.as_view()),
    path('list/', empmodels1API.as_view()),
    path('<int:pk>', empDetail.as_view()),
    path('list2/', cricketmodels2API.as_view()),
    path('cricketcreate/', cricketCreate.as_view()),
    path('c/''<int:pk>', cricketDetail.as_view()),
]

