from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index, name='index'),
    path('booktable/', views.get_booktable, name='booktable'),
    path('<int:year>/<str:month>', views.when_date, name="when_date")
]
