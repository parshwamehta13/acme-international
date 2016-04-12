
from django.conf.urls import include,url

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^employee/$', views.add_user, name='add_user'),     
    url(r'^viewemployee/add/$', views.employee_new, name='employee_new'),
    url(r'^home/$', views.visithome, name='visithome'),
    url(r'^viewtask/$', views.task_management, name='task_management'),
    url(r'^viewemployee/$', views.employee_list, name='employee_list'),
    url(r'^viewtask/add/$', views.task_new, name='task_new'),
    url(r'^logout/$',views.logout_user, name='logout_user'),
    url(r'^logistics/',include('logistics.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^trade/',include('trade.urls')),
    url(r'^retail/',include('retail.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)