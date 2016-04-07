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
		return str(self.invoice_number)

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
		return str(self.receipt_number)
