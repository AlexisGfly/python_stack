from django.urls import path     
from . import views
urlpatterns = [
    path('/', views.inicio),
    path('/nuevo', views.nuevo),
    path('/login', views.log),
    path('/register', views.reg)
]