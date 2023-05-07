from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# moduleprocessing 
from apps.moduleprocessing.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login),
    path('ship-list/',listPage),
    path('main-monitor/',mainPage),
    path('anti-terror-phase-control/',changeLevel),
    path('pirate-info/',getPirateData),
    path('anti-terror-control/',manualControl),
    path('ocean-report/',tmp),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)