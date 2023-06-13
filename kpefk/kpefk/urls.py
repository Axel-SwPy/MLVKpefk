from django.contrib import admin
from django.urls import path, include
from main.views import *
from word.views import *
from excel.views import *
from access.views import *
from web_tech.views import *
from django.conf.urls.static import static
from kpefk import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('word.urls')),
    path('', include('excel.urls')),
    path('', include('access.urls')),
    path('', include('web_tech.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)