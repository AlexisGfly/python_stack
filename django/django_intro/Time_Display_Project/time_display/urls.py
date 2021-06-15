from django.urls import path     
from . import views
urlpatterns = [
    path('', views.inicio1),
    path('time_display/', views.inicio2),
]