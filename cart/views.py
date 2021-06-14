from django.shortcuts import render
from .models import Cart, CartItem
# Create your views here.

def cart(request,ip):
    prods= CartItem.objects.all()#filter(userip=ip)
    print(request.session['userip'])
    return render(request, "cart.html", {'products':prods})
    