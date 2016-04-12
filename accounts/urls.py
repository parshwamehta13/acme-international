from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^accounts/accountlist/$', views.accounts_admin, name='accounts_admin'),
	url(r'^accounts/(?P<account_number>\w+)/editaccount/$', views.account_edit, name='account_edit'),
	url(r'^accounts/new/account/$', views.account_new, name='account_new'),
	url(r'^accounts/(?P<transaction>\w+)/transactions/$', views.show_transaction, name='show_transaction'),
	url(r'^accounts/new/transaction/$', views.transaction_new, name='account_transaction_new'),
]