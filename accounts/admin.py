from django.contrib import admin

# Register your models here.
from .models import Account, Transaction, EmployeeCash
class TransactionInLine (admin.TabularInline):
	model = Transaction
	extra = 0

class TransactionAdmin (admin.ModelAdmin):
	list_display = ('account_number','transaction_date','transaction_type','transaction_amount')

class AccountAdmin (admin.ModelAdmin):
	inlines = [TransactionInLine]
	list_display = ('id','account_number','currency_type','amount')

class EmployeeCashAdmin(admin.ModelAdmin):
	list_display = ('employee_number','transaction_date','account_number','amount_added')

admin.site.register(Account,AccountAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(EmployeeCash, EmployeeCashAdmin)