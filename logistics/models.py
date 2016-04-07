from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from homepage.models import Employee_Detail
from django.db.models.signals import post_save
# Create your models here.
class Truck (models.Model):
	truck_registration_number = models.CharField(max_length=20,primary_key=True)
	truck_driver = models.CharField(max_length=50)
	truck_type_choices = (('Semi-trailer','SEMI-TRAILER'),('Trailer','TRAILER'),('Box-Body','BOX-BODY'))
	truck_type = models.CharField(max_length=20,choices=truck_type_choices,default='TRAILER')
	
	def __str__(self):
		return self.truck_registration_number

class Trip (models.Model):
	truck_registration_number = models.ForeignKey(Truck,on_delete=models.CASCADE)
	trip_source = models.CharField(max_length=50,blank=True)
	trip_destination = models.CharField(max_length=50,blank=True)
	trip_distance = models.IntegerField(blank=True)
	trip_shipper = models.CharField(max_length=50,blank=True)
	trip_consignee = models.CharField(max_length=50,blank=True)
	trip_goods_type = models.CharField(max_length=50,blank=True)
	trip_container_number = models.CharField(max_length=50,blank=True)
	trip_weight = models.IntegerField(default=100)
	trip_start_date = models.DateField(default=datetime.date.today)
	trip_end_date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return str(self.id)

class Document (models.Model):
	upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
	name = models.CharField(max_length = 100,default="File")
	trip = models.ForeignKey(Trip,on_delete=models.CASCADE)

	def __str__ (self):
		return self.name

class Expense (models.Model):
	bill = models.FileField(upload_to='uploads/expense/%Y/%m/%d/',blank=True)
	amount = models.IntegerField(blank=True)
	reason = models.TextField(blank=True)
	trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
	employee = models.ForeignKey(Employee_Detail,default=2)

	def __str__(self):
		return str(self.trip.truck_registration_number)+" "+str(self.amount)

class TruckDocument (models.Model):
	truck = models.ForeignKey(Truck)
	document = models.FileField(upload_to='uploads/%Y/%m/%d/')
	document_name = models.CharField(max_length=30)

def update_cash_in_hand(sender, instance,**kwargs):
	instance.employee.cash_in_hand = instance.employee.cash_in_hand -  instance.amount
	instance.employee.save()

post_save.connect(update_cash_in_hand, sender=Expense)