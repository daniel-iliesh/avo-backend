from store.models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)