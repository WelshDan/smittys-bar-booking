from django.urls import path
from . import views

urlpatterns = [
    path('booktable/', views.reserve_table, name='reserve_table'),
]
