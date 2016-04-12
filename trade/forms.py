from django import forms

from .models import Good,Transaction,Goodssearch,Document,Transactionsearch

class GoodSearchForm(forms.ModelForm):

    class Meta:
        model = Goodssearch
        fields = ('good_search_item', 'good_type',)

class GoodForm(forms.ModelForm):

    class Meta:
        model = Good
        fields = ('good_type', 'good_quantity',)

class DocsForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('upload', 'name', 'transaction_number',)

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('reference_name','from_company','transaction_date','transaction_type','goods_type','goods_quantity')

class TransactionSearchForm(forms.ModelForm):

    class Meta:
        model = Transactionsearch
        fields = ('transaction_search_item', 'transaction_type',)