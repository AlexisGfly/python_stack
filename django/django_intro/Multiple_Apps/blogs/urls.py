from django.urls import path     
from . import views
urlpatterns = [
    path('', views.inicio),
    path('blogs/', views.index),
    path('blogs/new/', views.nuevo),
    path('blogs/create/', views.crear),
    path('blogs/<int:num_1>/', views.show),
    path('blogs/<int:num_1>/edit/', views.editar),
    path('blogs/<int:num_1>/delete/', views.destruir),
]