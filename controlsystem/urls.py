from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# moduleprocessing 
from apps.moduleprocessing.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login),
    path('list/',listPage),
    path('main/',mainPage),
    path('change/',changeLevel),
    path('getpirate/',getPirateData),
    path('manualcontrol/',manualControl),
    path('test/',tmp),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)