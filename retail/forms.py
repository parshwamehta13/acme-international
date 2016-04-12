from django import forms

from .models import Receipt,Invoice,Receiptsearch,Invoicesearch

class ReceiptForm(forms.ModelForm):

    class Meta:
        model = Receipt
        fields = ('receipt_number', 'date', 'receipt_from','amount_received','payment_for','payment_mode','credited_to','balance',)

class ReceiptSearchForm(forms.ModelForm):

    class Meta:
        model = Receiptsearch
        fields = ('receipt_search_item', 'receiptsearch_type',)

class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('invoice_number', 'date', 'invoiced_to','details','quantity','unit_price','total_price','vat',)

class InvoiceSearchForm(forms.ModelForm):

    class Meta:
        model = Invoicesearch
        fields = ('invoice_search_item', 'invoicesearch_type',)