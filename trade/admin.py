from django.contrib import admin

# Register your models here.

from .models import Good, Transaction, Document

class DocumentInline(admin.StackedInline):
	model = Document
	extra = 0

class TransactionAdmin(admin.ModelAdmin):
	inlines = [DocumentInline]
	list_display = ('id','reference_name','from_company','transaction_type','transaction_date','goods_type','goods_quantity')
	search_fields = ('transaction_type','transaction_date','goods_type__good_type','id','goods_quantity')

class GoodAdmin(admin.ModelAdmin):
	list_display = ('good_type','good_quantity')
	search_fields = ('good_type','good_quantity')

class DocumentAdmin (admin.ModelAdmin):
	list_display = ('upload','name','transaction_number')
	search_fields = ('upload','name','transaction_number__id')

admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Good,GoodAdmin)
