from django.contrib import admin

# Register your models here.

from .models import Employee_Detail, Task

class TaskAdmin(admin.ModelAdmin):
	list_display = ('assigned_to','task_description','assigned_on','deadline','status')
	search_fields = ('assigned_to__username','task_description','assigned_on','deadline','status')

class Employee_DetailAdmin(admin.ModelAdmin):
	list_display = ('user','salary','cash_in_hand')
	search_fields = ('user__username','salary','cash_in_hand')

admin.site.register(Employee_Detail,Employee_DetailAdmin)
admin.site.register(Task, TaskAdmin)
