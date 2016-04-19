from django import forms

from .models import Truck,Trip,Tripsearch,Trucksearch,Document,Expense

class TruckForm(forms.ModelForm):

    class Meta:
        model = Truck
        fields = ('truck_registration_number', 'truck_driver', 'truck_type',)


class DocsForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('upload', 'name', 'trip',)


class TruckSearchForm(forms.ModelForm):

    class Meta:
        model = Trucksearch
        fields = ('truck_search_item', 'truck_type',)


class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = ('truck_registration_number', 'trip_source', 'trip_distance','trip_shipper','trip_destination','trip_consignee','trip_goods_type','trip_container_number','trip_weight','trip_start_date','trip_end_date')
        field_classes = {
            
        }

class TripSearchForm(forms.ModelForm):

    class Meta:
        model = Tripsearch
        fields = ('trip_search_item', 'trip_type',)

class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('bill', 'amount','reason','trip')
    



	