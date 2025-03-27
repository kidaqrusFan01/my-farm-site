from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order

# Create your views here.

def home_list(request):
    return render(request, 'blog/home_list.html', {})


def about(request):
    return render(request, 'blog/about.html', {})

def service(request):
    return render(request, 'blog/service.html', {})

def product(request):
    return render(request, 'blog/product.html', {})

def contact(request):
    return render(request, 'blog/contact.html', {})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'blog/product.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(product=product, quantity=1)
    return redirect('cart')


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(product=product, quantity=1)
    return redirect('cart')

def cart(request):
    orders = Order.objects.all()
    return render(request, 'blog/cart.html', {'orders': orders})