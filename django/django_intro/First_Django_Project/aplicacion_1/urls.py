from django.urls import path     
from . import views
urlpatterns = [
    path('', views.inicio),
    path('blogs/', views.index),
    path('blogs/new/', views.index2),
    path('blogs/create/', views.create),
    path('blogs/<int:num_1>/', views.show),
    path('blogs/<int:num_1>/edit/', views.edit),
    path('blogs/<int:num_1>/delete/', views.destroy),
]