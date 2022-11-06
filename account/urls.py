from django.urls import path, include

from .views import signin, register, signout, forgotten_password, verify_email, reset_password
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('login', signin, name='login'),
  path('register', register, name='register'),
  path('logout', signout, name='logout'),
  path('forgotten_password', forgotten_password, name='forgotten_password'),
  path('verify_email/<str:email>', verify_email, name="verify_email"),
  path('reset_password', reset_password, name='reset_password')
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

