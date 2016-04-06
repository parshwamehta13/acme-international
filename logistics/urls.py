from django.conf.urls import include,url

from . import views

urlpatterns = [
    url(r'add_truck/$', views.add_truck, name='add_truck'),
    url(r'add_trip/$', views.add_trip, name='add_trip'), 
    url(r'add_expense/$', views.add_expense, name='add_expense'), 
    url(r'add_document/$', views.add_document, name='add_document'), 
    url(r'view_trips/$', views.view_trips, name='view_trips'),
    url(r'view_trucks/$', views.view_trucks, name='view_trucks'),
    url(r'view_documents/$', views.view_documents, name='view_documents'),
    url(r'view_expenses/$', views.view_expenses, name='view_expenses'),
]