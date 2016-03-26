from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^hello/$', views.index2, name='index2'),
    #url(r'^success/$',views.success, name='success'),
    url(r'^logout/$',views.logout_user, name='logout_user'),
]