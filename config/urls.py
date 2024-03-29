"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from content.views import Main, UploadFeed
from user import views
from .settings.base import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
import config.views

# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView
# from django.conf import settings

urlpatterns = [
    path('', config.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('main/', Main.as_view()),
    path('content/', include('content.urls')),
    path('user/', include('user.urls')),
    # path('favicon.ico', RedirectView.as_view(
    #     url=staticfiles_storage.url("favicon.ico"))),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
