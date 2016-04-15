from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save,pre_save
from homepage.models import Employee_Detail
#from django.contrib.auth.models import User

# Create your models here.
@python_2_unicode_compatible
class BankAccount (models.Model):
	account_number = models.CharField(max_length=30,unique=True)
	#currency_type_choices = (('Uganda Shilling','Uganda Shilling'),('USD','USD'),('Euro','Euro'),('Kenya Shillings','Kenya Shillings'),('Congolese Franc','Congolese Franc'),('Rwanda Franc',' Rwanda Franc'),('INR','INR'))
	#currency_type = models.CharField(max_length=20,choices=currency_type_choices,default='USD')
	account_holder = models.CharField(max_length=100,default='Company')
	bank = models.CharField(max_length=100)
	amount = models.PositiveIntegerField(default=0)	

	def __str__ (self):
		return str(self.account_number)

class BankAccountssearch(models.Model):
	account_search_item = models.CharField(max_length=300)
	account_search_by = (('account_number','Account Number'),('amount','Amount'))
	account_type = models.CharField(max_length=100,choices=account_search_by,default='Account Number')
	def __str__(self):
		return str(self.id)

@python_2_unicode_compatible
class Transaction (models.Model):
	account_number = models.ForeignKey(BankAccount,on_delete=models.CASCADE)
	transaction_date = models.DateField(default=datetime.date.today)
	transaction_details = models.TextField()
	transaction_type_choices = (('Debit','Debit'),('Credit','Credit'))
	payment_mode_choices = (('Cheque','Cheque'),('Cash','Cash'))
	payment_mode = models.CharField(max_length=30,choices=payment_mode_choices,default='Cash')
	transaction_type = models.CharField(max_length=10,choices=transaction_type_choices,default='Debit')
	transaction_amount = models.IntegerField()
	#account_balance = models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.account_number.account_number)+" "+str(self.transaction_type)+" "+str(self.transaction_amount)

@python_2_unicode_compatible
class EmployeeCashBook (models.Model):
	#employee = models.ForeignKey(User)
	employee_number = models.ForeignKey(Employee_Detail)
	account_number = models.ForeignKey(BankAccount)
	amount_added = models.IntegerField()
	transaction_date = models.DateField(default=datetime.date.today)
	transaction_details = models.TextField(blank=True)

	def __str__(self):
		return str(self.employee_number.user.username)+" "+str(self.amount_added)+" "+str(self.id)

def update_amount (sender, instance, **kwargs):
	if instance.transaction_type == 'Debit':
		instance.account_number.amount = instance.account_number.amount - instance.transaction_amount
	else:
		instance.account_number.amount = instance.account_number.amount + instance.transaction_amount
	instance.account_number.save()

post_save.connect(update_amount, sender=Transaction)

def update_cash_in_hand (sender, instance,**kwargs):
	instance.employee_number.cash_in_hand = instance.employee_number.cash_in_hand + instance.amount_added
	instance.account_number.amount = instance.account_number.amount - instance.amount_added
	instance.employee_number.save()
	instance.account_number.save()

post_save.connect(update_cash_in_hand, sender=EmployeeCashBook)

def check_transaction (sender,instance,**kwargs):
	if instance.transaction_type == 'Debit' and instance.account_number.amount - instance.transaction_amount < 0:
		raise Exception("Not enough balance")

pre_save.connect(check_transaction,sender=Transaction)
