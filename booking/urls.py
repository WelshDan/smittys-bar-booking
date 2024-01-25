from django.urls import path
from booking import views

urlpatterns = [
    path('reserve_table/', views.reserve_table, name='reserve_table'),
]
