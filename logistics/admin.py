from django.contrib import admin

# Register your models here.

from .models import Document,Truck,Trip,Expense, TruckDocument

class DocumentInline(admin.TabularInline):
	model = Document
	extra = 0

class ExpenseInline (admin.TabularInline):
	model = Expense
	extra = 0

class TruckDocumentInline (admin.TabularInline):
	model = TruckDocument
	extra = 0

class TripAdmin(admin.ModelAdmin):
	inlines = [DocumentInline,ExpenseInline]
	list_display = ('id','truck_registration_number','trip_source','trip_destination','trip_distance','trip_shipper','trip_consignee','trip_container_number','trip_weight','trip_start_date','trip_end_date','trip_goods_type')
	search_fields = ('id','trip_source','trip_destination','trip_start_date','trip_end_date','trip_goods_type','truck_registration_number__truck_registration_number')

class DocumentAdmin(admin.ModelAdmin):
	list_display = ('upload','name','trip')
	search_fields = ('name',)

class ExpenseAdmin (admin.ModelAdmin):
	list_display = ('bill','reason','amount','trip')
	search_fields = ('trip',)

class TruckAdmin (admin.ModelAdmin):
	inlines = [TruckDocumentInline]
	list_display = ('truck_registration_number','truck_driver','truck_type')
	search_fields = list_display

admin.site.register(Truck, TruckAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(Document,DocumentAdmin)
admin.site.register(Expense, ExpenseAdmin)