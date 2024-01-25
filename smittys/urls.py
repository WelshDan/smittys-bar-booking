from django.contrib import admin
from django.urls import path, include
from booking import views as booking_views
from users import views
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('base/', views.get_base, name='base'),
    path('booktable/', booking_views.reserve_table, name='booktable'),
    path('booking/', include('booking.urls')),
    path('users/', include('users.urls')),
]

# Admin titles and headings"
admin.site.index_title = "Smitty's Bar & Restaurant"
admin.site.site_header = "Smitty's Bar & Restaurant Admin"
admin.site.site_title = "Smitty's Bar & Restaurant Admin"

admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)