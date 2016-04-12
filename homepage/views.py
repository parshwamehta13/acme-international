from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import EmployeeSearchForm,TaskForm,EmployeeForm
from .models import Employee_Detail, Task
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
	if request.user.is_authenticated():
		user_logged = request.user
		group_logged = user_logged.groups.all()
		if group_logged[0].id == 2:
			return render(request,'homepage/fronthomepage.html',{})
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
				#print "Here"
				return HttpResponse("User is not active")
		else:
			#print "Im here"
			return render(request,'homepage/index.html',{'error_message':True})
	return render(request,'homepage/index.html')



# def success(request):
# 	if request.user.is_authenticated():
# 		user_logged = request.user
# 		group_logged = user_logged.groups.all()
# 		if group_logged[0].id == 2:
# 			return redirect ('/admin')
# 		else:
# 			task_list = Task.objects.filter(assigned_to=user_logged)
# 			return render(request,'homepage/success.html',{'task_list':task_list})
# 	else:
# 		return redirect(index)

def visithome(request):
	return render(request,'homepage/fronthomepage.html')

def logout_user(request):
	logout(request)
	return redirect(index)

def add_user(request):
	return redirect ('/admin/auth/user/add')

def employee_list(request):
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
			return render(request, 'homepage/employee_list.html', {'employees_list': employees_list,'form': form})
	else:
		employees_list = Employee_Detail.objects.all()
		form = EmployeeSearchForm()
	return render(request, 'homepage/employee_list.html', {'employees_list': employees_list,'form': form})
	

def employee_new(request):
	if request.method == "POST":
		form = EmployeeForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			post.save()
			return redirect(employee_list)
	else:
		form = EmployeeForm()
	return render(request, 'homepage/employee_edit.html', {'form': form})


@login_required
def task_management(request):
	task_list = Task.objects.all()
	return render(request, 'homepage/tasks_list.html', {'task_list': task_list})


@login_required
def task_new(request):
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			post.save()
			return redirect(task_management)
	else:
		form = TaskForm()
	return render(request, 'homepage/task_edit.html', {'form': form})




    
        
    
            
            
            
           
            
        
           

        



