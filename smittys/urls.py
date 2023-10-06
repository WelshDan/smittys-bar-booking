from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_index, name='index'),
    path('booktable/', views.get_booktable, name='booktable'),
    path('base/', views.get_base, name='base'),
    path('signup/', views.get_signup, name='signup'),
    path('login/', views.get_login, name='login'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('allauth.urls')),
]

# Admin titles and headings"
admin.site.index_title = "Smitty's Bar & Restaurant"
admin.site.site_header = "Smitty's Bar & Restaurant Admin"
admin.site.site_title = "Smitty's Bar & Restaurant Admin"
