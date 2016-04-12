from django.conf.urls import url

from . import views

urlpatterns = [
 	url(r'^trip/$', views.trips_admin, name='trips_admin'),
    url(r'^truck/$', views.trucks_admin, name='trucks_admin'),
    url(r'^truck/(?P<truck_registration_number>\w+)/edittruck/$', views.truck_edit, name='truck_edit'),
    url(r'^trip/(?P<truck_number>\w+)/edittrip/$', views.trip_edit, name='trip_edit'),
    url(r'^(?P<docs>\w+)/showdoc/$', views.show_docs, name='show_docs'),
    url(r'^new/truck/$', views.truck_new, name='truck_new'),
    url(r'^new/document/$', views.docs_new, name='docs_new'),
    url(r'^new/trip/$', views.trip_new, name='trip_new'),
    #url(r'^new/$', views.trip_new, name='trip_new'),
]