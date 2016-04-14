from django.contrib import admin

# Register your models here.
from .models import BankAccount, Transaction, EmployeeCashBook
class TransactionInLine (admin.TabularInline):
	model = Transaction
	extra = 0

class TransactionAdmin (admin.ModelAdmin):
	list_display = ('account_number','transaction_date','transaction_details','payment_mode','transaction_type','transaction_amount')

class BankAccountAdmin (admin.ModelAdmin):
	inlines = [TransactionInLine]
	list_display = ('account_number','account_holder','bank','amount')

class EmployeeCashBookAdmin(admin.ModelAdmin):
	list_display = ('employee_number','transaction_date','account_number','amount_added','transaction_details')

admin.site.register(BankAccount,BankAccountAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(EmployeeCashBook, EmployeeCashBookAdmin)