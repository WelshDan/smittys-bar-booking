from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('', views.get_index, name='index'),
    path('booktable/', views.get_booktable, name='booktable'),
    path('<int:year>/<str:month>', views.when_date, name="when_date")
]
