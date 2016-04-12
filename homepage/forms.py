from django import forms

from .models import Employee_Detail,Employeesearch,Task

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee_Detail
        fields = ('user', 'salary', 'cash_in_hand',)

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('assigned_to', 'task_description','assigned_on','deadline','status')

        

class EmployeeSearchForm(forms.ModelForm):

    class Meta:
        model = Employeesearch
        fields = ('employee_search_item', 'employeesearch_type',)

