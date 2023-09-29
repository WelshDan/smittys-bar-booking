from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('', views.get_index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('booktable/', views.get_booktable, name='booktable'),
    path('base/', views.get_base, name='base')
]
