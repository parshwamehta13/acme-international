from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import GoodForm,GoodSearchForm,TransactionSearchForm,TransactionForm,DocsForm
from django.shortcuts import get_object_or_404
from .models import Transaction,Good,Document
from django.contrib.auth.decorators import login_required

@login_required
def goods_admin(request):
	
	if request.method == "POST":
		form = GoodSearchForm(request.POST)

		if form.is_valid():
			searchitem = form.cleaned_data['good_search_item']
			goodtype = form.cleaned_data['good_type']
			good_list = Good.objects.filter(**{goodtype: searchitem})
			return render(request, 'trade/good_list.html', {'good_list': good_list,'form': form})
	else:
		good_list = Good.objects.all()

		form = GoodSearchForm()
	return render(request, 'trade/good_list.html', {'good_list': good_list,'form': form})

@login_required
def good_new(request):
    if request.method == "POST":
        form = GoodForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect(goods_admin)
    else:
        form = GoodForm()
    return render(request, 'trade/good_edit.html', {'form': form})


@login_required
def good_edit(request, goodid):
   
    good = Good.objects.get(id=goodid)
    print(good.id)
    
    if request.method == "POST":
        form = GoodForm(request.POST, instance=good)
        if form.is_valid():
            good = form.save(commit=True)
            
            good.save()
            return redirect('goods_admin')
            
    else:
        form = GoodForm(instance=good)
    return render(request, 'trade/good_edit.html', {'form': form})

@login_required
def transactions_admin(request):
    
    if request.method == "POST":
        form = TransactionSearchForm(request.POST)

        if form.is_valid():
            searchitem = form.cleaned_data['transaction_search_item']
            transactiontype = form.cleaned_data['transaction_type']
            transaction_list = Transaction.objects.filter(**{transactiontype: searchitem})
            return render(request, 'trade/transaction_list.html', {'transaction_list': transaction_list,'form': form})
    else:
        transaction_list = Transaction.objects.all()

        form = TransactionSearchForm()
    return render(request, 'trade/transaction_list.html', {'transaction_list': transaction_list,'form': form})

@login_required
def transaction_new(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect(transactions_admin)
    else:
        form = TransactionForm()
    return render(request, 'trade/transaction_edit.html', {'form': form})


@login_required
def transaction_edit(request, transid):
    
    transaction = Transaction.objects.get(id=transid)
    print(transaction.id)
    
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            transactions = form.save(commit=True)
            
            transactions.save()
            return redirect('transactions_admin')
            
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'trade/transaction_edit.html', {'form': form})


@login_required
def show_docs_t(request, docs):    
    docus = Document.objects.filter(transaction_number=docs)
    return render(request, 'trade/t_docs_list.html', {'docus': docus,'transaction_number':docs})
            
@login_required
def docs_new_t(request):
    if request.method == "POST":
        form = DocsForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=True)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect(transactions_admin)
    else:
        form = DocsForm()
    return render(request, 'trade/t_docs_edit.html', {'form': form})
















 
# Create your views here.