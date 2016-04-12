from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^trade/goodslist/$', views.goods_admin, name='goods_admin'),
	url(r'^trade/(?P<goodid>\w+)/editgood/$', views.good_edit, name='good_edit'),
	url(r'^trade/new/goods/$', views.good_new, name='good_new'),
	url(r'^trade/transactions/$', views.transactions_admin, name='transactions_admin'),
	url(r'^trade/(?P<transid>\w+)/edittransaction/$', views.transaction_edit, name='transaction_edit'),
	url(r'^trade/new/transaction/$', views.transaction_new, name='transaction_new'),
	url(r'^trade/(?P<docs>\w+)/showdoc/$', views.show_docs_t, name='show_docs_t'),
	url(r'^trade/new/document/$', views.docs_new_t, name='docs_new_t'),
 ]