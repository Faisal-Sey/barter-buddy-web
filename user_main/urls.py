from django.urls import path, include
from .views import dashboard, home, find_buddies
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', home, name='home'),
  path('dashboard', dashboard, name='dashboard'),
  path('find-buddy', find_buddies, name='find_buddy'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)