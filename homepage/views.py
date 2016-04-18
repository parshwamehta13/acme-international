from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import EmployeeSearchForm,TaskForm,EmployeeForm,TaskSearchForm,CashbookForm
from .models import Employee_Detail, Task
from accounts.models import EmployeeCashBook
from logistics.models import Expense
from logistics.views import trips_admin
from django.contrib.auth.decorators import login_required
from logistics.models import Trip
from logistics.forms import TripSearchForm

# Login Page
def index(request):
    if request.user.is_authenticated():
        user_logged = request.user
        group_logged = user_logged.groups.all()
        if group_logged[0].id == 2:
            return redirect(trips_admin)
        else:
            task_list = Task.objects.filter(assigned_to=user_logged)
            return render(request,'homepage/success.html',{'task_list':task_list})
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect(index)
            else:
                return HttpResponse("User is not active")
        else:
            return render(request,'homepage/index.html',{'error_message':True})
    return render(request,'homepage/index.html')

# Go to Homepage
def visithome(request):
    return render(request,'homepage/fronthomepage.html')

# Method to logout user
def logout_user(request):
    logout(request)
    return redirect(index)

# Method to add user in django admin
def add_user(request):
    return redirect ('/admin/auth/user/add')

# Method to Add Employee
def add_employee(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        if request.method=="POST":
            username=request.POST['username']
            email = request.POST['email']
            password = 'acmeinternational123'
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            salary = request.POST['salary']
            cash_in_hand = request.POST['cash_in_hand']
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            group = Group.objects.get(name='Employee')
            user.groups.add(group)
            employee_detail = Employee_Detail(user=user,salary=salary,cash_in_hand=cash_in_hand)
            employee_detail.save()
            return redirect(employee_list)
        else:
            return render (request,'homepage/add_employee.html',{'title':"Add Employee"})
    else:
        return redirect(index)

# Method to view all the employee and its detail
def employee_list(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        if request.method == "POST":
            form = EmployeeSearchForm(request.POST)
            if form.is_valid():
                searchitem = form.cleaned_data['employee_search_item']
                employeesearchtype = form.cleaned_data['employeesearch_type']
                if employeesearchtype == "user":
                    try:
                        users = User.objects.get(username=searchitem).pk
                        employees_list = Employee_Detail.objects.filter(user=users)
                    except ObjectDoesNotExist:
                        employees_list = []
                else:
                    employees_list = Employee_Detail.objects.filter(**{employeesearchtype: searchitem}).values()
                return render(request, 'homepage/employee_list.html', {'employees_list': employees_list,'form': form,'title':"Employee List"})
            else:
                employees_list = Employee_Detail.objects.all()
                form = EmployeeSearchForm()
                return render(request, 'homepage/employee_list.html', {'employees_list': employees_list,'form': form,'title':"Employee List"})
        else:
            employees_list = Employee_Detail.objects.all()
            form = EmployeeSearchForm()
        return render(request, 'homepage/employee_list.html', {'employees_list': employees_list,'form': form, 'title':"Employee List"})
    else:
        return redirect(index)

# Method to add new employee details
def employee_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        if request.method == "POST":
            form = EmployeeForm(request.POST)
            if form.is_valid():
                post = form.save(commit=True)
                return redirect(employee_list)
        else:
            form = EmployeeForm()
        return render(request, 'homepage/employee_edit.html', {'form': form,'title':"Add Employee Details"})
    else:
        return redirect(index)

# Mehtod to display all the tasks and query it
def task_management(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        if request.method == "POST":
            form = TaskSearchForm(request.POST)
            if form.is_valid():
                searchitem = form.cleaned_data['task_search_item']
                employeesearchtype = form.cleaned_data['tasksearch_type']
                if employeesearchtype == "assigned_to":
                    try:
                        users = User.objects.get(username=searchitem).pk
                        task_list = Task.objects.filter(assigned_to__icontains=users)
                    except ObjectDoesNotExist:
                        task_list = []
                else:
                    tasksearchtype = tasksearchtype+"__icontains"
                    task_list = Task.objects.filter(**{tasksearchtype: searchitem}).values()
                return render(request, 'homepage/tasks_list.html', {'task_list': task_list,'form': form,'title':"Task Management"})
            else:
                task_list = Task.objects.all()
                form = TaskSearchForm()
                return render(request, 'homepage/tasks_list.html', {'task_list': task_list,'form': form,'title':"Task Management"})
        else:
            task_list = Task.objects.all()
            form = TaskSearchForm()
        return render(request, 'homepage/tasks_list.html', {'task_list': task_list,'form': form,'title':"Task Management"})
    else:
        return redirect(index)

# Method to add a task
def task_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                post = form.save(commit=True)
                return redirect(task_management)
        else:
            form = TaskForm()
        return render(request, 'homepage/task_edit.html', {'form': form,'title':"Assign Task"})
    else:
        return redirect(index)

# Method for Employee to view his/her Trip
def view_trip(request):
    user_logged = request.user
    trip_list = Trip.objects.filter(truck_registration_number__truck_driver=user_logged)
    if request.method == "POST":
        form = TripSearchForm(request.POST)
        if form.is_valid():
            searchitem = form.cleaned_data['trip_search_item']
            triptype = form.cleaned_data['trip_type']+'__icontains'
            trip_list = Trip.objects.filter(**{triptype: searchitem})
            return render(request, 'homepage/success_1.html', {'trip_list': trip_list,'form': form})
    else:
        trip_list = Trip.objects.filter(truck_registration_number__truck_driver=user_logged)
        form = TripSearchForm()
        return render(request, 'homepage/success_1.html',{'trip_list':trip_list,'form':form})

# Method to edit a task
def task_edit(request, taskid):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        task = get_object_or_404(Task, id=taskid)
        print(task.pk)
        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                task = form.save(commit=True)
                return redirect('task_management')
        else:
            form = TaskForm(instance=task)
        return render(request, 'homepage/task_edit.html', {'form': form, 'title':"Edit Task"})
    else:
        return redirect(index)

# Method to show employee his/her Expense
def show_emptripexpenses(request,empid):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        expenses = Expense.objects.filter(employee=empid)
        return render(request, 'homepage/expenses_list_emp.html', {'expenses': expenses,'title':"Trip Expenses"})
    else:
        return redirect(index)

# Method to show employee his/her cashbook
def show_employeecashbook(request,empid):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        cashbook = EmployeeCashBook.objects.filter(employee_number__id=empid)
        return render(request, 'homepage/cashbook_list.html', {'cashbook': cashbook,'title':"Employee Cashbook"})
    else:
        return redirect(index)

# Method to add a new cashbook to employee
def cashbook_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        if request.method == "POST":        
            form = CashbookForm(request.POST)
            if form.is_valid():            
                post = form.save(commit=True)
                return redirect(employee_list)
        else:
            form = CashbookForm()
        return render(request, 'homepage/cashbook_edit.html', {'form': form,'title':"Add new Cashbook"})
    else:
        return redirect(index)

# Method to edit a cashbook
def cashbook_edit(request, cashbookid):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        cashbook = EmployeeCashBook.objects.get(id=cashbookid)
        if request.method == "POST":
            form = CashbookForm(request.POST, instance=cashbook)
            if form.is_valid():
                cash = form.save(commit=True)
                return redirect('employee_list')
                
        else:
            form = CashbookForm(instance=cashbook)
        return render(request, 'homepage/cashbook_edit.html', {'form': form,'title':"Edit Cashbook"})
    else:
        return redirect(index)

# Method to Delete Employee
def delete_employee(request,empid):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        query = Employee_Detail.objects.get(pk=empid)
        query = User.objects.get(pk=query.user.id)
        query.delete()
        return redirect('employee_list')
    else:
        return redirect(index)

# Method to delete task
def delete_task(request,did):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        query = Task.objects.get(pk=did)
        query.delete()
        return redirect('task_management')
    else:
        return redirect(index)
        
    
            
            
            
           
            
        
           

        



