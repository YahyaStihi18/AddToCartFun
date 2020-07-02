from django.shortcuts import render,get_object_or_404,redirect
from  django.views.generic import DetailView
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterFrom
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required





# Create your views here.

@login_required() 
def index(request):
    user = request.user
    items_sum = len(OrderItem.objects.filter(user = user, ordered=False)) 

    items = Item.objects.all()
    context = {'items':items,'items_sum':items_sum }

    return render(request,'app/index.html',context)

@login_required() 
def profile(request):
    user = request.user
    orders = Order.objects.filter(user = user,ordered=True)

    return render(request,'app/profile.html',{'orders':orders})
    

@login_required() 
def checkout(request):
    user = request.user
    items_sum = len(OrderItem.objects.filter(user = user, ordered=False)) 

    
    order = get_object_or_404(Order,user=user,ordered=False)
    items = OrderItem.objects.filter(user = user, ordered=False)
    return render(request,'app/checkout.html',{'items':items,'order':order,'items_sum':items_sum})


def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"new user '{username}' created seccefully")
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'app/register.html', {'form': form})


@login_required() 
def detail(request,pk):
    user = request.user
    items_sum = len(OrderItem.objects.filter(user = user, ordered=False))
    item = get_object_or_404(Item, pk=pk) 

    return render(request,'app/detail.html',{'item':item,'items_sum':items_sum})






def add_to_cart(request, pk):
    item = Item.objects.get(pk=pk)
    order_item, created = OrderItem.objects.get_or_create(item=item,user = request.user,ordered=False)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk):
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(user = request.user)
        order.items.add(order_item)
    return redirect('app:detail',pk=pk)




def remove_from_cart(request, pk):
    user = request.user
    item = OrderItem.objects.filter(pk=pk, user = user)
    item.delete()
    return redirect('app:checkout')



def add(request,pk):
    user = request.user
    orderItem = OrderItem.objects.get(pk=pk)
    orderItem.quantity += 1
    orderItem.save()
    return redirect('app:checkout')
def remove(request,pk):
    user = request.user
    orderItem = OrderItem.objects.get(pk=pk)
    orderItem.quantity += -1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return redirect('app:checkout')

