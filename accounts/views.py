from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BankAccountSearchForm,BankAccountForm,TransactionForm
from .models import BankAccount,Transaction,EmployeeCashBook
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def accounts_admin(request):
    
	if request.method == "POST":
		form = BankAccountSearchForm(request.POST)
		if form.is_valid():
			searchitemaccount = form.cleaned_data['account_search_item']
			accounttype = form.cleaned_data['account_type']
			search_type = 'icontains'
			accounttype = accounttype + "__" + search_type
			accounts_list = BankAccount.objects.filter(**{accounttype: searchitemaccount})
			return render(request, 'accounts/accounts_list.html', {'accounts_list': accounts_list,'form': form})			
		else:
			accounts_list = BankAccount.objects.all()
	else:
		accounts_list = BankAccount.objects.all()
		form = BankAccountSearchForm()
	return render(request, 'accounts/accounts_list.html', {'accounts_list': accounts_list,'form': form})


@login_required
def account_new(request):
    if request.method == "POST":
        form = BankAccountForm(request.POST)
        if form.is_valid():
           account = form.save(commit=True)
           account.save()
           return redirect(accounts_admin)
    else:
        form = BankAccountForm()
    return render(request, 'accounts/account_edit.html', {'form': form})


@login_required                       
def account_edit(request, account_number):
    account = get_object_or_404(BankAccount, account_number=account_number)
    
    if request.method == "POST":
        form = BankAccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save(commit=True)
            
            account.save()
            return redirect('accounts_admin')
    else:
        form = BankAccountForm(instance=account)
    return render(request, 'accounts/account_edit.html', {'form': form})


@login_required
def show_transaction(request, transaction):
    trans_list = Transaction.objects.filter(account_number__account_number=transaction)
    return render(request, 'accounts/transaction_list.html', {'trans_list': trans_list,'account_no':transaction})


@login_required
def transaction_new(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect(accounts_admin)
    else:
        form = TransactionForm()
    return render(request, 'accounts/transaction_edit.html', {'form': form})