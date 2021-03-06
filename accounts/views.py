from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BankAccountSearchForm,BankAccountForm,TransactionForm
from homepage.forms import CashbookForm
from .models import BankAccount,Transaction,EmployeeCashBook
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

# This method will allow us to view all the accounts details of the user. It will redirect to accounts_list.html page which will create the display
def accounts_admin(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
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
        return render(request, 'accounts/accounts_list.html', {'accounts_list': accounts_list,'form': form,'title':'Accounts Admin'})
    else:
        return redirect(index)

# This will allow us to create a new accounts entry by redirecting us to the account_edit.hmtl page which contains the form.

def account_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        if request.method == "POST":
            form = BankAccountForm(request.POST)
            if form.is_valid():
               account = form.save(commit=True)
               return redirect(accounts_admin)
        else:
            form = BankAccountForm()
        return render(request, 'accounts/account_edit.html', {'form': form,'title':'New Account'})
    else:
        return redirect(index)


  #This will allow us to edit any of the details that is stored in an account. It identifies the account by matching account_number to its django assigned id
def account_edit(request,account_number):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        account = get_object_or_404(BankAccount, account_number=account_number)
        
        if request.method == "POST":
            form = BankAccountForm(request.POST, instance=account)
            if form.is_valid():
                account = form.save(commit=True)
                return redirect('accounts_admin')
        else:
            form = BankAccountForm(instance=account)
        return render(request, 'accounts/account_edit.html', {'form': form,'title':'Edit Account'})
    else:
        return redirect(index)


# This will allow us to view transactions made from or to a particular account. It identifies the account by comapine the transaction value  to its unique id.
def show_transaction(request, transaction):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        trans_list = Transaction.objects.filter(account_number__account_number=transaction)
        return render(request, 'accounts/transaction_list.html', {'trans_list': trans_list,'account_no':transaction,'title':'Transaction Log'})
    else:
        return redirect(index)    

#This view will allow us to create a new transaction by redirecting us to transaction_edit.html page which contains the form
def transaction_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        if request.method == "POST":
            form = TransactionForm(request.POST)
            if form.is_valid():
                post = form.save(commit=True)
                return redirect(accounts_admin)
        else:
            form = TransactionForm()
        return render(request, 'accounts/transaction_edit.html', {'form': form,'title':'New Transaction'})
    else:
        return redirect(index)
# This will allow us to view all the cashbooks.
def show_employeecashbook_all(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        cashbook = EmployeeCashBook.objects.all()
        return render(request, 'accounts/cashbook_list_all.html', {'cashbook': cashbook,'title':'Employee Cashbook'})
    else:
        return redirect(index)
#This will alow us to create a new cashbook
def cashbook_new_all(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        if request.method == "POST":        
            form = CashbookForm(request.POST)
            if form.is_valid():            
                post = form.save(commit=True)
                return redirect('show_employeecashbook_all')
        else:
            form = CashbookForm()
        return render(request, 'accounts/cashbook_edit_all.html', {'form': form,'title':'New Employee CashBook'})
    else:
        return redirect(index)

#This will allow us to edit the details of the cashbook
def cashbook_edit_all(request, cashbookid):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        cashbook = EmployeeCashBook.objects.get(id=cashbookid)            
        if request.method == "POST":
            form = CashbookForm(request.POST, instance=cashbook)
            if form.is_valid():
                cash = form.save(commit=True)
                return redirect('show_employeecashbook_all')                
        else:
            form = CashbookForm(instance=cashbook)
        return render(request, 'accounts/cashbook_edit_all.html', {'form': form,'title':'Edit CashBook'})
    else:
        return redirect(index)