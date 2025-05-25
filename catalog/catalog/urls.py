"""catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path, reverse_lazy
from django.views.generic.base import RedirectView

from node.views import listNodes

# from user.urls import project_urls as pu
# from node.urls import project_urls as puN
# from category.urls import project_urls as puC

from django.conf import settings
from django.conf.urls.static import static

import json
from catalog.color import color
from catalog.lib import dump

urlpatterns = [
    path('', listNodes, name='listNodes'),
    path('', include("user.urls")),
    path('node/', include("node.urls")),
    path('category/', include("category.urls")),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
urlpatterns += static('downloads/', document_root=settings.DOWNLOADS_ROOT)
# urlpatterns += pu
# urlpatterns += puN
# urlpatterns += puC
