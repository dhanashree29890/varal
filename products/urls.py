from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('products', views.products, name='products'),
    path('contact', views.contact, name='contact'),
    path('buynow/<int:id>', views.buy, name='buynow'),
    path('addtocart/<int:id>', views.addtocart, name='addtocart'),
    path('success', views.success, name='success'),
    path('failure', views.failure, name='failure'),
]
