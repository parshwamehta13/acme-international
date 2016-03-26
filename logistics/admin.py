from django.contrib import admin

# Register your models here.

from .models import Document,Truck,Trip,Expense

class DocumentInline(admin.TabularInline):
	model = Document
	extra = 0

class ExpenseInline (admin.TabularInline):
	model = Expense
	extra = 0

class TripAdmin(admin.ModelAdmin):
	inlines = [DocumentInline,ExpenseInline]
	list_display = ('id','trip_source','trip_destination','trip_date','trip_goods_type','truck_registration_number')
	search_fields = ('id','trip_source','trip_destination','trip_date','trip_goods_type','truck_registration_number__truck_registration_number')

class DocumentAdmin(admin.ModelAdmin):
	list_display = ('upload','name','trip')
	search_fields = ('name',)

class ExpenseAdmin (admin.ModelAdmin):
	list_display = ('bill','reason','amount','trip')
	search_fields = ('trip',)

admin.site.register(Truck)
admin.site.register(Trip, TripAdmin)
admin.site.register(Document,DocumentAdmin)
admin.site.register(Expense, ExpenseAdmin)