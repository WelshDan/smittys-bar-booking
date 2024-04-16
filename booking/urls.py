from django.urls import path
from booking import views
from .views import reserve_table

urlpatterns = [
    path('reserve_table/', views.reserve_table, name='reserve_table'),
    path('get_bookings/', views.get_bookings, name='get_bookings')
]
