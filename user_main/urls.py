from django.urls import path, include

from .views import dashboard, home, find_buddies, get_profile, create_connection, account_settings, accept_connection, get_connection
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', home, name='home'),
  path('dashboard', dashboard, name='dashboard'),
  path('find-buddy', find_buddies, name='find_buddy'),
  path('get-profile', get_profile, name='get_profile'),
  path('create-connection', create_connection, name='create_connection'),
  path('account_settings', account_settings, name='account_settings'),
  path('accept-connection', accept_connection, name='accept_connection'),
  path('get-connection', get_connection, name='get_connection'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)