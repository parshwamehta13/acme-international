from django import forms

from .models import Employee_Detail,Employeesearch,Task,Tasksearch
from accounts.models import EmployeeCashBook

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

class TaskSearchForm(forms.ModelForm):

    class Meta:
        model = Tasksearch
        fields = ('task_search_item', 'tasksearch_type',)

class CashbookForm(forms.ModelForm):

    class Meta:
        model = EmployeeCashBook
        fields = ('employee_number', 'account_number','amount_added','transaction_date','transaction_details',)
