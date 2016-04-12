from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ReceiptForm,ReceiptSearchForm,InvoiceForm,InvoiceSearchForm
from django.shortcuts import get_object_or_404
from .models import Invoice,Receipt
from django.contrib.auth.decorators import login_required



@login_required
def receipts_admin(request):
    if request.method == "POST":
		form = ReceiptSearchForm(request.POST)
		if form.is_valid():
			searchitemreceipt = form.cleaned_data['receipt_search_item']
			receipttype = form.cleaned_data['receiptsearch_type']
            #search_type = 'icontains'
            #receipttype = receipttype + "__" + search_type
			receipt_list = Receipt.objects.filter(**{receipttype: searchitemreceipt})
			return render(request, 'retail/receipts_list.html', {'receipt_list': receipt_list,'form': form})			
        #else:
            #receipt_list = Receipt.objects.all()
    else:
        receipt_list = Receipt.objects.all()
        form = ReceiptSearchForm()
	return render(request, 'retail/receipts_list.html', {'receipt_list': receipt_list,'form': form})


@login_required
def receipt_new(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=True)
            #post.author = request.user
            #post.published_date = timezone.now()
            receipt.save()
            return redirect(receipts_admin)
    else:
        form = ReceiptForm()
    return render(request, 'retail/receipt_edit.html', {'form': form})


@login_required           
def receipt_edit(request, receipt_number):
    receipt = get_object_or_404(Receipt, id=receipt_number)
   
    if request.method == "POST":
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            receipt = form.save(commit=True)
            
            receipt.save()
            return redirect('receipts_admin')
    else:
        form = ReceiptForm(instance=receipt)
    return render(request, 'retail/receipt_edit.html', {'form': form})


@login_required
def invoices_admin(request):
	if request.method == "POST":
		form = InvoiceSearchForm(request.POST)
		if form.is_valid():
			searchiteminvoice = form.cleaned_data['invoice_search_item']
			invoicetype = form.cleaned_data['invoicesearch_type']
            #search_type = 'icontains'
            #invoicetype = receipttype + "__" + search_type
			invoice_list = Invoice.objects.filter(**{invoicetype: searchiteminvoice})
			return render(request, 'retail/invoices_list.html', {'invoice_list': invoice_list,'form': form})
        #else:
            #invoice_list = Invoice.objects.all()
    #else:
		#invoice_list = Invoice.objects.all()
		#form = InvoiceSearchForm()
	#return render(request, 'retail/invoices_list.html', {'invoice_list': invoice_list,'form': form})









def invoice_new(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=True)
            #post.author = request.user
            #post.published_date = timezone.now()
            invoice.save()
            return redirect(invoices_admin)
    else:
        form = InvoiceForm()
    return render(request, 'retail/invoice_edit.html', {'form': form})
           
def invoice_edit(request, invoice_number):
    invoice = get_object_or_404(Invoice, id=invoice_number)
    
    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save(commit=True)
            
            invoice.save()
            return redirect('invoices_admin')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'retail/invoice_edit.html', {'form': form})