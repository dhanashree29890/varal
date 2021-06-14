from django.urls import path

from . import views

urlpatterns = [
    path('<str:ip>', views.cart, name='cart'),
    #path('buynow/<int:id>', views.buy, name='buynow'),
   
]
