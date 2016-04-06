from django import forms

from .models import Truck, Trip, Document, Expense

class TruckForm(forms.ModelForm):

    class Meta:
        model = Truck
        fields = ('truck_registration_number', 'truck_driver', 'truck_type',)

class TripForm (forms.ModelForm):

	class Meta:
		model = Trip
		fields = '__all__'

class DocumentForm(forms.ModelForm):
	
	class Meta:
		model = Document
		fields = '__all__'

class ExpenseForm(forms.ModelForm):
	
	class Meta:
		model = Expense
		fields = '__all__'