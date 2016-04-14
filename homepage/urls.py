
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
    url(r'^(?P<empid>\w+)/showexpenses/$', views.show_emptripexpenses, name='show_emptripexpenses'),
    url(r'^(?P<empid>\w+)/showcashbook/$', views.show_employeecashbook, name='show_employeecashbook'),
    url(r'^(?P<empid>\w+)/deleteemployee/$', views.delete_employee, name='delete_employee'),
    url(r'^(?P<did>\w+)/deletetask/$', views.delete_task, name='delete_task'),
    url(r'^(?P<cashbookid>\w+)/editcashbook/$', views.cashbook_edit, name='cashbook_edit'),
    url(r'^addcashbook/$', views.cashbook_new, name='cashbook_new'),
    url(r'^(?P<taskid>\w+)/edittask/$', views.task_edit, name='task_edit'),
    url(r'^viewtask/add/$', views.task_new, name='task_new'),
    url(r'^logout/$',views.logout_user, name='logout_user'),
    url(r'^addemployee/$',views.add_employee, name='add_employee'),
    url(r'^logistics/',include('logistics.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^trade/',include('trade.urls')),
    url(r'^retail/',include('retail.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)