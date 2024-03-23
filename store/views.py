from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Cart, CartItem, Collection, Customer, Order, OrderItem, Product
import json

# List all collections or create a new one (GET, POST)
@csrf_exempt
def collection_list(request):
    if request.method == 'GET':
        collections = list(Collection.objects.values())  # convert QuerySet to list to serialize
        return JsonResponse(collections, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        collection = Collection.objects.create(**data)
        return JsonResponse({'id': collection.id}, status=201)

# Retrieve, update, or delete a specific collection (GET, PUT, DELETE)
@csrf_exempt
def collection_detail(request, id):
    collection = get_object_or_404(Collection, id=id)
    if request.method == 'GET':
        return JsonResponse({'id': collection.id, 'name': collection.name})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        Collection.objects.filter(id=id).update(**data)
        return JsonResponse({'message': 'Collection was updated'})
    elif request.method == 'DELETE':
        collection.delete()
        return JsonResponse({'message': 'Collection was deleted'})

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = list(Product.objects.values())  # convert QuerySet to list to serialize
        return JsonResponse(products, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(**data)
        return JsonResponse({'id': product.id}, status=201)

# Retrieve, update, or delete a specific product (GET, PUT, DELETE)
@csrf_exempt
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        return JsonResponse({'id': product.id, 'name': product.name})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        Product.objects.filter(id=id).update(**data)
        return JsonResponse({'message': 'Product was updated'})
    elif request.method == 'DELETE':
        Product.delete()
        return JsonResponse({'message': 'Product was deleted'})

@csrf_exempt
def customer_list(request):
    if request.method == 'GET':
        customers = list(Customer.objects.values())  # convert QuerySet to list to serialize
        return JsonResponse(customers, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        customer = Customer.objects.create(**data)
        return JsonResponse({'id': customer.id}, status=201)

# Retrieve, update, or delete a specific customer (GET, PUT, DELETE)
@csrf_exempt
def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'GET':
        return JsonResponse({'id': customer.id, 'name': customer.name})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        Customer.objects.filter(id=id).update(**data)
        return JsonResponse({'message': 'Customer was updated'})
    elif request.method == 'DELETE':
        Customer.delete()
        return JsonResponse({'message': 'Customer was deleted'})

@csrf_exempt
def cart_list(request):
    if request.method == 'GET':
        carts = list(Cart.objects.values())  # convert QuerySet to list to serialize
        return JsonResponse(carts, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        cart = Cart.objects.create(**data)
        return JsonResponse({'id': cart.id}, status=201)

# Retrieve, update, or delete a specific cart (GET, PUT, DELETE)
@csrf_exempt
def cart_detail(request, id):
    cart = get_object_or_404(Cart, id=id)
    if request.method == 'GET':
        return JsonResponse({'id': cart.id, 'name': cart.name})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        Cart.objects.filter(id=id).update(**data)
        return JsonResponse({'message': 'Cart was updated'})
    elif request.method == 'DELETE':
        Cart.delete()
        return JsonResponse({'message': 'Cart was deleted'})

@csrf_exempt
def cart_item_list(request):
    if request.method == 'GET':
        cart_items = list(CartItem.objects.values())  # convert QuerySet to list to serialize
        return JsonResponse(cart_items, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        cart_item = CartItem.objects.create(**data)
        return JsonResponse({'id': cart_item.id}, status=201)

# Retrieve, update, or delete a specific cart_item (GET, PUT, DELETE)
@csrf_exempt
def cart_item_detail(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    if request.method == 'GET':
        return JsonResponse({'id': cart_item.id, 'name': cart_item.name})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        CartItem.objects.filter(id=id).update(**data)
        return JsonResponse({'message': 'CartItem was updated'})
    elif request.method == 'DELETE':
        CartItem.delete()
        return JsonResponse({'message': 'CartItem was deleted'})

@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        orders = list(Order.objects.values())  # convert QuerySet to list to serialize
        return JsonResponse(orders, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.create(**data)
        return JsonResponse({'id': order.id}, status=201)

# Retrieve, update, or delete a specific order (GET, PUT, DELETE)
@csrf_exempt
def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'GET':
        return JsonResponse({'id': order.id, 'name': order.name})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        Order.objects.filter(id=id).update(**data)
        return JsonResponse({'message': 'Order was updated'})
    elif request.method == 'DELETE':
        Order.delete()
        return JsonResponse({'message': 'Order was deleted'})

@csrf_exempt
def order_item_list(request):
    if request.method == 'GET':
        order_items = list(OrderItem.objects.values())  # convert QuerySet to list to serialize
        return JsonResponse(order_items, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        order_item = OrderItem.objects.create(**data)
        return JsonResponse({'id': order_item.id}, status=201)

# Retrieve, update, or delete a specific order_item (GET, PUT, DELETE)
@csrf_exempt
def order_item_detail(request, id):
    order_item = get_object_or_404(OrderItem, id=id)
    if request.method == 'GET':
        return JsonResponse({'id': order_item.id, 'name': order_item.name})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        OrderItem.objects.filter(id=id).update(**data)
        return JsonResponse({'message': 'OrderItem was updated'})
    elif request.method == 'DELETE':
        OrderItem.delete()
        return JsonResponse({'message': 'OrderItem was deleted'})
