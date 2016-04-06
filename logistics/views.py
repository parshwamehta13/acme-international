from django.shortcuts import render
from django.http import HttpResponse
from .forms import TruckForm, TripForm, DocumentForm, ExpenseForm
from .models import Truck, Trip, Expense, Document

# Create your views here.

def add_truck (request):
	if request.method == 'POST':
		form = TruckForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Saved")
		else:
			return HttpResponse("Wrong Entry")
	else:
		form = TruckForm()
	return render(request, 'logistics/add_truck.html', {'form': form})

def add_trip (request):
	if request.method == 'POST':
		form = TripForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Saved")
		else:
			return HttpResponse("Wrong Entry")
	else:
		form = TripForm()
	return render(request, 'logistics/add_trip.html', {'form': form})

def add_document (request):
	if request.method == 'POST':
		form = TripForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Saved")
		else:
			return HttpResponse("Wrong Entry")
	else:
		form = DocumentForm()
	return render(request, 'logistics/add_document.html', {'form': form})

def add_expense (request):
	if request.method == 'POST':
		form = TripForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Saved")
		else:
			return HttpResponse("Wrong Entry")
	else:
		form = ExpenseForm()
	return render(request, 'logistics/add_expense.html', {'form': form})

def view_trips (request):
	if 'query' in request.GET and request.GET['query']:
		q = request.GET['query']
		trips = []
		trips = list(Trip.objects.filter(truck_registration_number__truck_registration_number__icontains=q)) + list(Trip.objects.filter(trip_source__icontains=q)) + list(Trip.objects.filter(trip_destination__icontains=q)) + list(Trip.objects.filter(trip_date__icontains=q))
	else:
		trips = Trip.objects.all()
	return render(request,'logistics/view_trips.html',{'trips':trips})

def view_documents (request):
	documents = Document.objects.all()
	return render(request,'logistics/view_documents.html',{'documents': documents})

def view_trucks (request):
	trucks = Truck.objects.all()
	return render(request,'logistics/view_trucks.html',{'trucks':trucks})

def view_expenses (request):
	expenses = Expense.objects.all()
	return render(request,'logistics/view_expenses.html',{'expenses':expenses})