from django.urls import path
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.get_indexpage, name='indexpage'),
    path('booktable/', views.get_booktable, name='booktable'),
    path('basepage/', views.get_basepage, name='basepage')
]
