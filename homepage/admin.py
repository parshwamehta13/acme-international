from django.contrib import admin

# Register your models here.

from .models import Employee_Detail, Task
from accounts.models import EmployeeCashBook

class TaskAdmin(admin.ModelAdmin):
	list_display = ('assigned_to','task_description','assigned_on','deadline','status','priority')
	search_fields = ('assigned_to__username','task_description','assigned_on','deadline','status','priority')

class EmployeeCashBookInline(admin.TabularInline):
	model = EmployeeCashBook
	extra = 0

class Employee_DetailAdmin(admin.ModelAdmin):
	inlines = [EmployeeCashBookInline]
	list_display = ('user','salary','cash_in_hand')
	search_fields = ('user__username','salary','cash_in_hand')

admin.site.register(Employee_Detail,Employee_DetailAdmin)
admin.site.register(Task, TaskAdmin)
