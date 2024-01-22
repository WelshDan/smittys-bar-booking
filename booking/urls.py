from django.urls import path
from . import views

urlpatterns = [
    path('booktable/', views.get_booktable, name='booktable'),
]
