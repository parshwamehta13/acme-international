from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .models import Employee_Detail, Task
# Create your views here.

def index(request):
	if request.user.is_authenticated():
		user_logged = request.user
		group_logged = user_logged.groups.all()
		if group_logged[0].id == 2:
			return redirect ('/admin')
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

def logout_user(request):
	logout(request)
	return redirect(index)