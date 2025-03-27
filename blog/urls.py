from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_list, name='home_list'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('product', views.product, name='product'),
    path('contact', views.contact, name='contact'),
    path('product_list', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),

]