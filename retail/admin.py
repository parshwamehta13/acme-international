from django.contrib import admin
from .models import Invoice, Receipt
# Register your models here.

class InvoiceAdmin (admin.ModelAdmin):
	list_display = ('invoice_number','date','invoiced_to','details','quantity','unit_price','total_price','vat')
	search_fields = list_display

class ReceiptAdmin (admin.ModelAdmin):
	list_display = ('receipt_number','date','receipt_from','amount_received','payment_for','payment_mode_choices','payment_mode','credited_to','balance')
	search_fields = ('receipt_number','date','receipt_from','amount_received','payment_for','payment_mode_choices','payment_mode','credited_to__account_number','balance')

admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Receipt,ReceiptAdmin)
