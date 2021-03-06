"""orderdjangorest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from ordermodelrest import views
from ordermodelrest.views import MerchViewEnabled
# from rest_framework import settings
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'merch/photo', views.PhotoView, 'photo')
router.register(r'merch', views.MerchView, 'merch')
#router.register(r'photo', views.PhotoView, 'photos')
router.register(r'mercher', views.MerchingView, 'mercher')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url('^mercing/(?P<merch_enabled>.+)/$', MerchViewEnabled.as_view()),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
