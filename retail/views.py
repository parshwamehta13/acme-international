from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ReceiptForm,ReceiptSearchForm,InvoiceForm,InvoiceSearchForm
from django.shortcuts import get_object_or_404
from .models import Invoice,Receipt
from django.contrib.auth.decorators import login_required


def receipts_admin(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        if request.method == "POST":
            form = ReceiptSearchForm(request.POST)
            if form.is_valid():
                searchitemreceipt = form.cleaned_data['receipt_search_item']
                receipttype = form.cleaned_data['receiptsearch_type']+"__icontains"
                receipt_list = Receipt.objects.filter(**{receipttype: searchitemreceipt})
                return render(request, 'retail/receipts_list.html', {'receipt_list': receipt_list,'form': form,'title':'Receipt Admin'})            
        else:
            receipt_list = Receipt.objects.all()
            form = ReceiptSearchForm()
        return render(request, 'retail/receipts_list.html', {'receipt_list': receipt_list,'form': form,'title':'Receipt Admin'})
    else:
        return redirect(index)


def receipt_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        if request.method == "POST":
            form = ReceiptForm(request.POST)
            if form.is_valid():
                receipt = form.save(commit=True)
                return redirect(receipts_admin)
        else:
            form = ReceiptForm()
        return render(request, 'retail/receipt_edit.html', {'form': form,'title':'Add New Receipt'})
    else:
        return redirect(index)
           
def receipt_edit(request, receipt_number):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        receipt = get_object_or_404(Receipt, id=receipt_number)       
        if request.method == "POST":
            form = ReceiptForm(request.POST, instance=receipt)
            if form.is_valid():
                receipt = form.save(commit=True)
                return redirect('receipts_admin')
        else:
            form = ReceiptForm(instance=receipt)
        return render(request, 'retail/receipt_edit.html', {'form': form,'title':'Edit Receipt'})
    else:
        return redirect(index)

def invoices_admin(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:    
        if request.method == "POST":
            form = InvoiceSearchForm(request.POST)
            if form.is_valid():
                searchiteminvoice = form.cleaned_data['invoice_search_item']
                invoicetype = form.cleaned_data['invoicesearch_type']+"__icontains"
                invoice_list = Invoice.objects.filter(**{invoicetype: searchiteminvoice})
                return render(request, 'retail/invoices_list.html', {'invoice_list': invoice_list,'form': form,'title':'Invoice Admin'})
            else:
                invoice_list = Invoice.objects.all()
        else:
            invoice_list = Invoice.objects.all()
            form = InvoiceSearchForm()
        return render(request, 'retail/invoices_list.html', {'invoice_list': invoice_list,'form': form,'title':'Invoice Admin'})
    else:
        return redirect(index)


def invoice_new(request):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        if request.method == "POST":
            form = InvoiceForm(request.POST)
            if form.is_valid():
                invoice = form.save(commit=True)
                return redirect(invoices_admin)
        else:
            form = InvoiceForm()
        return render(request, 'retail/invoice_edit.html', {'form': form,'title':'Add Invoice'})
    else:
        return redirect(index)
          
def invoice_edit(request, invoice_number):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        invoice = get_object_or_404(Invoice, id=invoice_number)
        
        if request.method == "POST":
            form = InvoiceForm(request.POST, instance=invoice)
            if form.is_valid():
                invoice = form.save(commit=True)
                return redirect('invoices_admin')
        else:
            form = InvoiceForm(instance=invoice)
        return render(request, 'retail/invoice_edit.html', {'form': form,'title':'Edit Invoice'})
    else:
        return redirect(index)

 
def delete_invoice(request,did):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        query = Invoice.objects.get(pk=did)
        query.delete()
        return redirect('invoices_admin')
    else:
        return redirect(index)
 
def delete_receipt(request,did):
    if request.user.is_authenticated() and request.user.groups.all()[0].id==2:
        query = Receipt.objects.get(pk=did)
        query.delete()
        return redirect('receipts_admin')
    else:
        return redirect(index)