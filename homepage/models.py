from __future__ import unicode_literals
from django.contrib.auth.models import User
import datetime
from django.db import models

# Create your models here.

class Employee_Detail(models.Model):
	user = models.ForeignKey(User)
	salary = models.IntegerField()
	cash_in_hand = models.IntegerField(default=0)

	def __str__(self):
		return str(self.user.username)

class Task (models.Model):
	assigned_to = models.ForeignKey(User)
	task_description = models.TextField()
	assigned_on = models.DateField(default=datetime.date.today)
	deadline = models.DateField()
	status = models.BooleanField(default=False)

	def __str__(self):
		return str(self.assigned_to.username)+" "+str(self.assigned_on)+" "+str(self.status)