from __future__ import unicode_literals
import datetime
from django.db import models
from accounts.models import BankAccount
# Create your models here.

class Invoice (models.Model):
	invoice_number = models.IntegerField()
	date = models.DateField(default=datetime.date.today)
	invoiced_to = models.CharField(max_length=100)
	details = models.TextField(blank=True)
	quantity = models.IntegerField()
	unit_price = models.IntegerField()
	total_price = models.IntegerField()
	vat = models.IntegerField()

	def __str__ (self):
		return str(self.invoice_number)+" "+str(self.id)

class Receipt (models.Model):
	receipt_number = models.IntegerField()
	date = models.DateField(default=datetime.date.today)
	receipt_from = models.CharField(max_length=100)
	amount_received = models.IntegerField()
	payment_for = models.ForeignKey(Invoice)
	payment_mode_choices = (('Cheque','Cheque'),('Cash','Cash'))
	payment_mode = models.CharField(max_length=30,choices=payment_mode_choices,default='Cash')
	credited_to = models.ForeignKey(BankAccount)
	balance = models.IntegerField()

	def __str__ (self):
		return str(self.receipt_number)+" "+str(self.id)

class Receiptsearch(models.Model):
	receipt_search_item = models.CharField(max_length=300)
	receipt_search_by = (('receipt_number','Receipt Number'),('receipt_from','Receipt From'),('payment_mode','Payment Mode'),('credited_to','Credited To'),('balance','Balance'),('date','Date'))
	receiptsearch_type = models.CharField(max_length=20,choices=receipt_search_by)
	def __str__(self):
		return str(self.id)

class Invoicesearch(models.Model):
	invoice_search_item = models.CharField(max_length=300)
	invoice_search_by = (('invoice_number','Invoice Number'),('date','Date'),('invoiced_to','Invoiced To'),('quantity','Quantity'),('unit_price','Unit Price'),('total_price','Total Price'),('vat','VAT'))
	invoicesearch_type = models.CharField(max_length=20,choices=invoice_search_by)
	def __str__(self):
		return str(self.id)