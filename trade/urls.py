from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^goodslist/$', views.goods_admin, name='goods_admin'),
	url(r'^(?P<goodid>\w+)/editgood/$', views.good_edit, name='good_edit'),
	url(r'^new/goods/$', views.good_new, name='good_new'),
	url(r'^transactions/$', views.transactions_admin, name='transactions_admin'),
	url(r'^(?P<transid>\w+)/edittransaction/$', views.transaction_edit, name='transaction_edit'),
	url(r'^new/transaction/$', views.transaction_new, name='transaction_new'),
	url(r'^(?P<docs>\w+)/showdoc/$', views.show_docs_t, name='show_docs_t'),
	url(r'^new/document/$', views.docs_new_t, name='docs_new_t'),
 ]