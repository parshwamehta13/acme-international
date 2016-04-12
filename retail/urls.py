from django.conf.urls import url

from . import views

urlpatterns = [
 url(r'^retail/receiptlist/$', views.receipts_admin, name='receipts_admin'),
 url(r'^retail/(?P<receipt_number>\w+)/receiptgood/$', views.receipt_edit, name='receipt_edit'),
  url(r'^retail/new/receipts/$', views.receipt_new, name='receipt_new'),
  url(r'^retail/invoicelist/$', views.invoices_admin, name='invoices_admin'),
 url(r'^retail/(?P<invoice_number>\w+)/editinvoice/$', views.invoice_edit, name='invoice_edit'),
  url(r'^retail/new/invoice/$', views.invoice_new, name='invoice_new'),
   
 ]