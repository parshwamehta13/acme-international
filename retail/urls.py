from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^invoicelist/$', views.invoices_admin, name='invoices_admin'),
	url(r'^receiptlist/$', views.receipts_admin, name='receipts_admin'),
	url(r'^(?P<receipt_number>\w+)/receiptgood/$', views.receipt_edit, name='receipt_edit'),
	url(r'^new/receipts/$', views.receipt_new, name='receipt_new'),
  	url(r'^(?P<did>\w+)/deleteinvoice/$', views.delete_invoice, name='delete_invoice'),
  	url(r'^(?P<did>\w+)/deletereceipt/$', views.delete_receipt, name='delete_receipt'),
 	url(r'^(?P<invoice_number>\w+)/editinvoice/$', views.invoice_edit, name='invoice_edit'),
  	url(r'^new/invoice/$', views.invoice_new, name='invoice_new'),
   
 ]