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
		return str(self.user.username)+" "+str(self.salary)

class Task (models.Model):
	assigned_to = models.ForeignKey(User)
	task_description = models.TextField(blank=True)
	assigned_on = models.DateField(default=datetime.date.today)
	deadline = models.DateField()
	status = models.BooleanField(default=False)
	priority_choices = (('Urgent','Urgent'),('Normal Priority','Normal Priority'),('Low Priority','Low Priority'))
	priority = models.CharField(max_length=20,choices=priority_choices,default='Normal Priority')

	def __str__(self):
		return str(self.assigned_to.username)+" "+str(self.assigned_on)+" "+str(self.status)+" "+str(self.id)

class Employeesearch(models.Model):
	employee_search_item = models.CharField(max_length=300)
	employee_search_by = (('salary','Salary'),('user','Employee name'))
	employeesearch_type = models.CharField(max_length=20,choices=employee_search_by)
	
	def __str__(self):
		return str(self.id)

class Tasksearch(models.Model):
	task_search_item = models.CharField(max_length=300)
	task_search_by = (('assigned_to','Assigned To'),('assigned_on','Assigned on'),('deadline','Deadline'))
	tasksearch_type = models.CharField(max_length=20,choices=task_search_by)
	def __str__(self):
		return str(self.id)