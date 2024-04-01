from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('collections/', views.collection_list, name='collection_list'),  # GET, POST
    path('collections/<int:id>/', views.collection_detail, name='collection_detail'),  # GET, PUT, DELETE
    
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:id>/', views.customer_detail, name='customer_detail'),

    path('carts/', views.cart_list, name='cart_list'),
    path('carts/<int:id>/', views.cart_detail, name='cart_detail'),

    path('cart_items/', views.cart_item_list, name='cart_item_list'),
    path('cart_items/<int:id>/', views.cart_item_detail, name='cart_item_detail'),
    
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:id>/', views.order_detail, name='order_detail'),

    path('order_items/', views.order_item_list, name='order_item_list'),
    path('order_items/<int:id>/', views.order_item_detail, name='order_item_detail'),
]