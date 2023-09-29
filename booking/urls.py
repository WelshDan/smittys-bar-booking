from django.urls import path
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.get_index, name='index'),
    path('booktable/', views.get_booktable, name='booktable'),
    path('base/', views.get_base, name='base'),
    path('login/', views.get_login, name='login')
]
