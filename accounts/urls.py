from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^accountlist/$', views.accounts_admin, name='accounts_admin'),
	url(r'^(?P<account_number>\w+)/editaccount/$', views.account_edit, name='account_edit'),
	url(r'^new/account/$', views.account_new, name='account_new'),
	url(r'^(?P<transaction>\w+)/transactions/$', views.show_transaction, name='show_transaction'),
	url(r'^new/transaction/$', views.transaction_new, name='account_transaction_new'),
	url(r'^(?P<cashbookid>\w+)/editcashbook/$', views.cashbook_edit_all, name='cashbook_edit_all'),
    url(r'^addcashbook/$', views.cashbook_new_all, name='cashbook_new_all'),
    url(r'^viewcashbook/$', views.show_employeecashbook_all, name='show_employeecashbook_all'),
]