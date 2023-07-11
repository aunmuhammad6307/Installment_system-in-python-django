from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'accounts/index.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def customer_list(request):
    customer_list = Installment.objects.all()
    context = {
        'customer_list' : customer_list
    }
    return render(request, 'accounts/customer_list.html', context)

def all_accounts(request):
    customer = Order.objects.all().order_by('-order_ID')
    context = {
        'customer' : customer
    }
    return render(request, 'accounts/all_accounts.html', context)

def all_order_list(request):
    customer = Order.objects.all().order_by('-order_ID')
    context = {
        'customer' : customer
    }
    return render(request, 'accounts/all_order_list.html', context)

def customer_profile(request, pk_text):
    customer = Order.objects.get(customer_id= pk_text)
    receipt = Receipt.objects.filter(customer_id = pk_text)
    order = Customer.objects.get(id=pk_text)
    orders = order.order_set.all()
    order_count = orders.count()
    context = {
        'customer' : customer,
        'all_order' : order_count,
        'orders' : orders,
        'order' : order,
        'receipt' : receipt
    }
    return render(request, 'accounts/customer.html', context)
