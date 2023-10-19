
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

# This is the namespace for the app
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
