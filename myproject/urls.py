"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/',include('homepage.urls')),
    url(r'^logistics/',include('logistics.urls')),
    url(r'^passreset/$',auth_views.password_reset,name='forgot_password1'),
    url(r'^passresetdone/$',auth_views.password_reset_done,name='password_reset_done'),
    url(r'^passresetconfirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',auth_views.password_reset_confirm,name='password_reset_confirm'),
    url(r'^passresetcomplete/$',auth_views.password_reset_complete,name='password_reset_complete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
