"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
import logging
#import debug_toolbar

logging.getLogger('command').debug(' >>> ' + __name__)
logging.getLogger('command').debug('STATIC_ROOT = ' + settings.STATIC_ROOT)
logging.getLogger('command').debug('MEDIA_ROOT = ' + settings.MEDIA_ROOT)

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^', include(('macuos.urls', 'macuos'), namespace='macuos'))
   #url(r'^__debug__/', include(debug_toolbar.urls))
   #url(r'^macuos/', include(('macuos.urls', 'macuos'), namespace='macuos')),
   #url(r'^media/(?P<path>.*)$', serve, {'media_root': settings.MEDIA_ROOT}),
   #pattern('', (r'^media/(?P.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}))
]

#if settings.DEBUG:
#urlpatterns += pattern('', (r'^media/(?P.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}))
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += pattern('', (r'^media/(?P.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}))
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
   import debug_toolbar
   urlpatterns = [
      url(r'^__debug__/', include(debug_toolbar.urls))
   ] + urlpatterns
