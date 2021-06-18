from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('op_1_casino', views.casino_1),
    path('op_2_casino', views.casino_2),
    path('op_3_casino', views.casino_3),
    path('op_4_casino', views.casino_4),
    path('process_money',views.procesa_oro),
    path('reset',views.restore)
]