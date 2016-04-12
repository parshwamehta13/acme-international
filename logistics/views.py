
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TruckForm,TripForm,TripSearchForm,TruckSearchForm,DocsForm
from django.shortcuts import get_object_or_404
from .models import Truck,Trip,Document,Expense
from django.contrib.auth.decorators import login_required


@login_required
def trucks_admin(request):
	if request.method == "POST":
		form = TruckSearchForm(request.POST)
		if form.is_valid():
			searchitemtruck = form.cleaned_data['truck_search_item']
			trucktype = form.cleaned_data['truck_type']
			#search_type = 'icontains'
			#trucktype = trucktype + "__" + search_type
			truck_list = Truck.objects.filter(**{trucktype: searchitemtruck})
			return render(request, 'logistics/trucks_list.html', {'truck_list': truck_list,'form': form})			
		else:
			truck_list = Truck.objects.all()
	else:
		truck_list = Truck.objects.all()
		form = TruckSearchForm()
	return render(request, 'logistics/trucks_list.html', {'truck_list': truck_list,'form': form})


@login_required
def trips_admin(request):	
	if request.method == "POST":
		form = TripSearchForm(request.POST)
		if form.is_valid():
			searchitem = form.cleaned_data['trip_search_item']
			triptype = form.cleaned_data['trip_type']
			search_type = 'icontains'
			triptype = triptype + "__" + search_type
			trip_list = Trip.objects.filter(**{triptype: searchitem})
			return render(request, 'logistics/trips_list.html', {'trip_list': trip_list,'form': form})
		else:
			trip_list = Trip.objects.all()
	else:
		trip_list = Trip.objects.all()

		form = TripSearchForm()
	return render(request, 'logistics/trips_list.html', {'trip_list': trip_list,'form': form})


@login_required
def truck_new(request):
	if request.method == "POST":
		form = TruckForm(request.POST)
		if form.is_valid():
			truck = form.save(commit=True)
			truck.save()
			return redirect(trucks_admin)
	else:
		form = TruckForm()
	return render(request, 'logistics/truck_edit.html', {'form': form})


@login_required		   
def truck_edit(request, truck_registration_number):
	truck = get_object_or_404(Truck, id=truck_registration_number)
	print(truck.pk)
	if request.method == "POST":
		form = TruckForm(request.POST, instance=truck)
		if form.is_valid():
			truck = form.save(commit=True)            
			truck.save()
			return redirect('trucks_admin')
	else:
		form = TruckForm(instance=truck)
	return render(request, 'logistics/truck_edit.html', {'form': form})

@login_required
def trip_new(request):
	if request.method == "POST":
		form = TripForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			post.save()
			return redirect(trips_admin)
	else:
		form = TripForm()
	return render(request, 'logistics/trip_edit.html', {'form': form})


@login_required
def trip_edit(request, truck_number):
	print(truck_number)
	trip = Trip.objects.get(id=truck_number)
	print(trip.truck_registration_number)    
	if request.method == "POST":
		form = TripForm(request.POST, instance=trip)
		if form.is_valid():
			trip = form.save(commit=True)
			
			trip.save()
			return redirect('trips_admin')
			
	else:
		form = TripForm(instance=trip)
	return render(request, 'logistics/trip_edit.html', {'form': form})


@login_required
def show_docs(request, docs):    
	docus = Document.objects.filter(trip=docs)
	return render(request, 'logistics/docs_list.html', {'docus': docus})			

@login_required			
def docs_new(request):
	if request.method == "POST":        
		form = DocsForm(request.POST, request.FILES)
		if form.is_valid():            
			post = form.save(commit=True)
			post.save()
			return redirect(trips_admin)
	else:
		form = DocsForm()
	return render(request, 'logistics/docs_edit.html', {'form': form})   