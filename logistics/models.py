from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from homepage.models import Employee_Detail
from django.db.models.signals import post_save
# Create your models here.

# Model for Truck
class Truck (models.Model):
	truck_registration_number = models.CharField(max_length=20,unique=True)
	truck_driver = models.ForeignKey(User)
	truck_type_choices = (('Semi-trailer','SEMI-TRAILER'),('Trailer','TRAILER'),('Box-Body','BOX-BODY'))
	truck_type = models.CharField(max_length=20,choices=truck_type_choices,default='TRAILER')
	
	def __str__(self):
		return self.truck_registration_number+" "+str(self.id)

# Model for Trip
class Trip (models.Model):
	truck_registration_number = models.ForeignKey(Truck)
	trip_source = models.CharField(max_length=50,blank=True)
	trip_destination = models.CharField(max_length=50,blank=True)
	trip_distance = models.PositiveIntegerField(blank=True)
	trip_shipper = models.CharField(max_length=50,blank=True)
	trip_consignee = models.CharField(max_length=50,blank=True)
	trip_goods_type = models.CharField(max_length=50,blank=True)
	trip_container_number = models.CharField(max_length=50,blank=True)
	trip_weight = models.PositiveIntegerField(default=100,blank=True)
	trip_start_date = models.DateField(default=datetime.date.today,blank=True)
	trip_end_date = models.DateField(default=datetime.date.today,blank=True)

	def __str__(self):
		return str(self.id)

# Model for Trip Document
class Document (models.Model):
	upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
	name = models.CharField(max_length = 100,default="File")
	trip = models.ForeignKey(Trip)

	def __str__ (self):
		return self.name

# Model for Trip Expense
class Expense (models.Model):
	bill = models.FileField(upload_to='uploads/expense/%Y/%m/%d/',blank=True)
	amount = models.DecimalField(max_digits=12,decimal_places=2)
	reason = models.TextField(blank=True)
	trip = models.ForeignKey(Trip)

	def __str__(self):
		return str(self.trip.truck_registration_number)+" "+str(self.amount)

# Model for Truck Document
class TruckDocument (models.Model):
	truck = models.ForeignKey(Truck)
	document = models.FileField(upload_to='uploads/%Y/%m/%d/')
	document_name = models.CharField(max_length=30)

# Method for changing value of cash in hand during expense
def update_cash_in_hand(sender, instance,**kwargs):
	instance.employee.cash_in_hand = instance.employee.cash_in_hand -  instance.amount
	instance.employee.save()

post_save.connect(update_cash_in_hand, sender=Expense)

# Model for Truck Searching
class Tripsearch(models.Model):
	trip_search_item = models.CharField(max_length=300)
	trip_search_by = (('trip_source','Trip Source'),('trip_start_date','Trip Start Date'),('trip_end_date','Trip End Date'),('trip_destination','Trip Destination'),('trip_goods_type','Goods Type'),('trip_container_number','Container Number'))
	trip_type = models.CharField(max_length=100,choices=trip_search_by,default='Trip Source')
	def __str__(self):
		return str(self.id)

# Model for Truck Searching
class Trucksearch(models.Model):
	truck_search_item = models.CharField(max_length=300)
	truck_search_by = (('truck_registration_number','Truck registration number'),('truck_type','Truck Type'))
	truck_type = models.CharField(max_length=100,choices=truck_search_by,default='Truck Driver')
	def __str__(self):
		return str(self.id)
	