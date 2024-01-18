from django.contrib import admin
from django.urls import path, include
from booking import views
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.get_index, name='index'),
    path('base/', views.get_base, name='base'),
    path('booking/', include('booking.urls')),
    path('booktable/', views.get_booktable, name='booktable'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]

# Admin titles and headings"
admin.site.index_title = "Smitty's Bar & Restaurant"
admin.site.site_header = "Smitty's Bar & Restaurant Admin"
admin.site.site_title = "Smitty's Bar & Restaurant Admin"
