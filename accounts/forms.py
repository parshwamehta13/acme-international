from django import forms

from .models import BankAccount,Transaction,BankAccountssearch

class BankAccountSearchForm(forms.ModelForm):

    class Meta:
        model = BankAccountssearch
        fields = ('account_search_item', 'account_type',)

class BankAccountForm(forms.ModelForm):

    class Meta:
        model = BankAccount
        fields = ('account_number','account_holder','bank', 'amount',)


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('account_number','transaction_date','transaction_details','transaction_type','transaction_amount',)