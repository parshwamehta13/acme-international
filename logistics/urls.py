from django.conf.urls import url

from . import views

urlpatterns = [
 	url(r'^trip/$', views.trips_admin, name='trips_admin'),
    url(r'^truck/$', views.trucks_admin, name='trucks_admin'),
    url(r'^truck/(?P<truck_registration_number>\w+)/edittruck/$', views.truck_edit, name='truck_edit'),
    url(r'^trip/(?P<truck_number>\w+)/edittrip/$', views.trip_edit, name='trip_edit'),
    url(r'^(?P<docs>\w+)/showdoc/$', views.show_docs, name='show_docs'),
    url(r'^new/truck/$', views.truck_new, name='truck_new'),
    url(r'^(?P<tripid>\w+)/showexpenses/$', views.show_tripexpenses, name='show_tripexpenses'),
    url(r'^(?P<did>\w+)/deletetruck/$', views.delete_truck, name='delete_truck'),
    url(r'^(?P<did>\w+)/deletetrip/$', views.delete_trip, name='delete_trip'),
    url(r'^new/expenseall/$', views.tripexpenses_new_all, name='tripexpenses_new_all'),
    url(r'^new/document/$', views.docs_new, name='docs_new'),
    url(r'^new/expense/$', views.tripexpenses_new, name='tripexpenses_new'),
    url(r'^showexpenses/$', views.show_tripexpenses_all, name='views.show_tripexpenses_all'),
    url(r'^(?P<expenseid>\w+)/showexpenses/$', views.tripexpenses_edit, name='tripexpense_edit'),
    url(r'^new/trip/$', views.trip_new, name='trip_new'),
    url(r'^new_employee/trip/$', views.trip_new_employee, name='trip_new_employee'),
    url(r'^new_employee/document/$', views.docs_new_employee, name='docs_new_employee'),
    url(r'^(?P<docs>\w+)/showdocemployee/$', views.show_docs_employee, name='show_docs_employee'),
]