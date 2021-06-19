from django.urls import path     
from . import views
urlpatterns = [
    path('/', views.inicio),
    path('/nuevo', views.nuevo)
]