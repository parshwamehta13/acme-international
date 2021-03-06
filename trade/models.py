from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
# Create your models here.

#This is a model for all the details of the goods that are owned .
@python_2_unicode_compatible
class Good(models.Model):
	good_type = models.CharField(max_length=100,default='Oil')
	good_quantity = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.good_type

#This model will allow us to store all the data reagring a particular transaction. It is directly related to the goods model
@python_2_unicode_compatible
class Transaction (models.Model):
	reference_name = models.CharField(max_length=100)
	from_company = models.CharField(max_length=100,blank=True)
	transaction_date = models.DateField(default=datetime.date.today)
	transaction_type = models.CharField(max_length=10,choices=(('Import','Import'),('Export','Export')),default='Import')
	goods_type = models.ForeignKey(Good)
	goods_quantity = models.IntegerField(default=0)
	def __str__ (self):
		return self.transaction_type+" "+str(self.id)

#This model will allow us to search for goods according to their fields.
class Goodssearch(models.Model):
	good_search_item = models.CharField(max_length=300)
	good_search_by = (('good_type','Good Type'),('good_quantity','Good Quantity'))
	good_type = models.CharField(max_length=100,choices=good_search_by,default='Good Type')
	def __str__(self):
		return str(self.id)
#This model will allow us to search for transaction according to their fields.		
class Transactionsearch(models.Model):
	transaction_search_item = models.CharField(max_length=300)
	transaction_search_by = (('reference_name','Reference Name'),('from_company','Import Company'),('transaction_type','Transaction type'),('transaction_date','Transaction Date'))
	transaction_type = models.CharField(max_length=100,choices=transaction_search_by,default='Transaction Type')
	def __str__(self):
		return str(self.id)
#This store all the fields that are required for storing a document
@python_2_unicode_compatible
class Document (models.Model):
	upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
	name = models.CharField(max_length = 100,default="File")
	transaction_number = models.ForeignKey(Transaction)

	def __str__ (self):
		return self.name
#Will update the goods in case of import or export
def update_goods (sender, instance, **kwargs):
	if instance.transaction_type=='Import':
		instance.goods_type.good_quantity = instance.goods_type.good_quantity+instance.goods_quantity
	else:
		instance.goods_type.good_quantity = instance.goods_type.good_quantity-instance.goods_quantity
	instance.goods_type.save()

post_save.connect(update_goods, sender=Transaction)