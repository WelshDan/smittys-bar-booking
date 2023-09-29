"""smittys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.get_indexpage, name='indexpage'),
    path('booktable/', views.get_booktable, name='booktable'),
    path('basepage/', views.get_basepage, name='basepage')
]

# Admin titles and headings"
admin.site.index_title = "Smitty's Bar & Restaurant"
admin.site.site_header = "Smitty's Bar & Restaurant Admin"
admin.site.site_title = "Smitty's Bar & Restaurant Admin"
