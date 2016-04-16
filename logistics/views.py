
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TruckForm,TripForm,TripSearchForm,TruckSearchForm,DocsForm, ExpenseForm
from django.shortcuts import get_object_or_404
from .models import Truck,Trip,Document,Expense
from django.contrib.auth.decorators import login_required

#This function will display the list of truks present in the data base. truck_List is the list of all objets of the type model Truck which is then passed to the template trucks_list.html . This function will a
#also respond to search queries that request to filter data according to a particual field of the model truck. searchitemtruck will obtain the value that should be matched
#and trucktype will obtain the value of the field that that will be use for filtering
def trucks_admin(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        if request.method == "POST":
            form = TruckSearchForm(request.POST)
            if form.is_valid():
                searchitemtruck = form.cleaned_data['truck_search_item']
                trucktype = form.cleaned_data['truck_type']+"__icontains"
                truck_list = Truck.objects.filter(**{trucktype: searchitemtruck})
                return render(request, 'logistics/trucks_list.html', {'truck_list': truck_list,'form': form})
            else:
                truck_list = Truck.objects.all()
                form = TruckSearchForm()
                return render(request, 'logistics/trucks_list.html', {'truck_list': truck_list,'form': form})            
        else:
            truck_list = Truck.objects.all()
            form = TruckSearchForm()
        return render(request, 'logistics/trucks_list.html', {'truck_list': truck_list,'form': form,'title':"Trucks Admin"})
    else:
        return redirect('index')


#It first checks if a search form has been submitted. It yes then the list of trips that will be displayed has to be filted according to the query.triptype will
#obtain the field name i,e the column that should be accesed while matching the query and searchitem will obtain the entry in the table in column triptype that
#should be matched with all the items in the column.
#If no search form has been submitted then all the objects of type Trip are stored in list trip_list and passed to template trips_lit.html

def trips_admin(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        if request.method == "POST":
            form = TripSearchForm(request.POST)
            if form.is_valid():
                searchitem = form.cleaned_data['trip_search_item']
                triptype = form.cleaned_data['trip_type']+"__icontains"
                trip_list = Trip.objects.filter(**{triptype: searchitem})
                return render(request, 'logistics/trips_list.html', {'trip_list': trip_list,'form': form,'title':"Trips Admin"})
            else:
                trip_list = Trip.objects.all()
        else:
            trip_list = Trip.objects.all()

            form = TripSearchForm()
        return render(request, 'logistics/trips_list.html', {'trip_list': trip_list,'form': form,'title':"Trip Admin"})
    else:
        return redirect('index')


#This function will allow us to create a new entry of truck. It checks first if the user is asking for a blank form or has filled the form and os asking to save it.
#If the user is asking to save the form then the form is saved using form.save() and then the page redirected to the template pointed by the view trucks_admin.
#If the user is asking for a new from then the form assigned for the truck i.e TruckFomr() is saved as form and then passed in the template truck_edit. This template
# will open the form for us.
def truck_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        if request.method == "POST":
            form = TruckForm(request.POST)
            if form.is_valid():
                truck = form.save(commit=True)
                return redirect(trucks_admin)
        else:
            form = TruckForm()
        return render(request, 'logistics/truck_edit.html', {'form': form, 'title':"Add Truck",'operation':'New'})
    else:
        return redirect('index')


#This function will accept the argument truck_registration_number . This argument stores the value of unique truck id so that we can obtain the particular instance of
# of the truck. On obtaining the instance of truck we can then access the truck form with the values filled in with the respective fields of that instance of truck.
#On making a change and clicking the save button the form is saved with updated values and again redirected to trucks_admin.         
def truck_edit(request, truck_registration_number):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        truck = get_object_or_404(Truck, id=truck_registration_number)
        print(truck.pk)
        if request.method == "POST":
            form = TruckForm(request.POST, instance=truck)
            if form.is_valid():
                truck = form.save(commit=True)            
                return redirect('trucks_admin')
        else:
            form = TruckForm(instance=truck)
        return render(request, 'logistics/truck_edit.html', {'form': form, 'title':"Edit Truck Details",'operation':'Edit'})
    else:
        return redirect('index')

#This function will allow us to create a new entry of trip. It checks first if the user is asking for a blank form or has filled the form and os asking to save it.
#If the user is asking to save the form then the form is saved using form.save() and then the page redirected to the template pointed by the view trips_admin.
#If the user is asking for a new from then the form assigned for the trip i.e tripFomr() is saved as form and then passed in the template trip_edit. This template
# will open the form for us.
def trip_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        if request.method == "POST":
            form = TripForm(request.POST)
            if form.is_valid():
                post = form.save(commit=True)
                return redirect(trips_admin)
        else:
            form = TripForm()
        return render(request, 'logistics/trip_edit.html', {'form': form,'title':"Add Trip",'operation':'New'})
    else:
        return redirect('index')

#This function will accept the argument trip_registration_number . This argument stores the value of unique trip id so that we can obtain the particular instance of
# of the trip. On obtaining the instance of trip we can then access the trip form with the values filled in with the respective fields of that instance of trip.
#On making a change and clicking the save button the form is saved with updated values and again redirected to trips_admin. 

def trip_edit(request, truck_number):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        print(truck_number)
        trip = Trip.objects.get(id=truck_number)
        print(trip.truck_registration_number)    
        if request.method == "POST":
            form = TripForm(request.POST, instance=trip)
            if form.is_valid():
                trip = form.save(commit=True)
                return redirect('trips_admin')
                
        else:
            form = TripForm(instance=trip)
        return render(request, 'logistics/trip_edit.html', {'form': form,'title':"Edit Trip"})
    else:
        return redirect('index')

#This function will let us view the docs related to the instance of trip that is passes as an argument. docs agrument will store the id of the trip 
#whose documents we wish to access. 
def show_docs(request, docs):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:     
        docus = Document.objects.filter(trip=docs)
        return render(request, 'logistics/docs_list.html', {'docus': docus,'title':"View Documents"})            
    else:
        return redirect('index')     

# Method to create a new Trip Document
def docs_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        if request.method == "POST":        
            form = DocsForm(request.POST, request.FILES)
            if form.is_valid():            
                post = form.save(commit=True)
                return redirect(trips_admin)
        else:
            form = DocsForm()
        return render(request, 'logistics/docs_edit.html', {'form': form,'title':"Add Document",'operation':'New'})   
    else:
        return redirect('index')

# Method to create a show expense of particular trip
def show_tripexpenses(request,tripid):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        expenses = Expense.objects.filter(trip=tripid)
        return render(request, 'logistics/expenses_list.html', {'expenses': expenses,'title':"View Expenses"})
    else:
        return redirect('index')                   

# Method to add an expense
def tripexpenses_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        if request.method == "POST":
            
            form =ExpenseForm(request.POST, request.FILES)   
            if form.is_valid():
                post = form.save(commit=True)
                return redirect(trips_admin)
        else:
            form = ExpenseForm()
        return render(request, 'logistics/expense_edit.html', {'form': form,'title':"Add Trip Expense",'operation':'New'})
    else:
        return redirect('index')

# Method to delete a truck
def delete_truck(request,did):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        query = Truck.objects.get(pk=did)        
        query.delete()
        return redirect('trucks_admin')
    else:
        return redirect('index')


# Method to delete a trip
def delete_trip(request,did):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        query = Trip.objects.get(pk=did)        
        query.delete()
        return redirect('trips_admin')
    else:
        return redirect('index')


# Method to show all trip expenses
def show_tripexpenses_all(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:     
        expenses = Expense.objects.all()
        return render(request, 'logistics/expenses_list_all.html', {'expenses': expenses,'title':"All Expenses"})
    else:
        return redirect('index')                    


# Method to add new expenses to employee 
def tripexpenses_new_all(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        if request.method == "POST":            
            form =ExpenseForm(request.POST, request.FILES)   
            if form.is_valid():
                post = form.save(commit=True)
                return redirect('show_tripexpenses_all')
        else:
            form = ExpenseForm()
        return render(request, 'logistics/expense_edit_all.html', {'form': form,'title':"Add Expense",'operation':'New'})
    else:
        return redirect('index')


# Method to Edit Trip Expense
def tripexpenses_edit(request, expenseid):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2: 
        expense = Expense.objects.get(id=expenseid)         
        if request.method == "POST":
            form = ExpenseForm(request.POST, instance=expense)
            if form.is_valid():
                expense = form.save(commit=True)
                return redirect('show_tripexpenses_all')                
        else:
            form = ExpenseForm(instance=expense)
        return render(request, 'logistics/logistics/expense_edit_all.html', {'form': form,'title':"Edit Trip Expense",'operation':'Edit'})
    else:
        return redirect('index')


# Method to view trips- Employee Login
def trips_employee(request):
    if request.method == "POST":
            form = TripSearchForm(request.POST)

            if form.is_valid():
                searchitem = form.cleaned_data['trip_search_item']
                triptype = form.cleaned_data['trip_type']
                trip_list = Trip.objects.filter(**{triptype: searchitem})
                return render(request, 'logistics/trips_list.html', {'trip_list': trip_list,'form': form})
    else:
        trip_list = Trip.objects.filter(truck_registration_number__truck_driver=request.user)

        form = TripSearchForm()
        return render(request, 'logistics/trips_list_employee.html', {'trip_list': trip_list,'form': form})


# Method to add new trip by Employee
def trip_new_employee(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('index')
    else:
        form = TripForm()
    return render(request, 'logistics/trip_edit_employee.html', {'form': form})     

# Method to show documents of a particular trip
def show_docs_employee(request, docs):
    
    docus = Document.objects.filter(trip=docs)
    return render(request, 'logistics/doc_list_employee.html', {'docus': docus})
            
# Method to add a new document by an Employee            
def docs_new_employee(request):
    if request.method == "POST":
        
        form = DocsForm(request.POST, request.FILES)
        if form.is_valid():    
        
            post = form.save(commit=True)
            return redirect('index')
    else:
        form = DocsForm()
    return render(request, 'logistics/doc_edit_employee.html', {'form': form}) 