from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('random_word',views.palabra_aleatoria),
    path('reset',views.restore)
]