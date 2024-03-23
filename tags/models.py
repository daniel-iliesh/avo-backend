from django.db import models
from store.models import Product

# Create your models here.
class Tag(models.Model):
    label = models.TextField()
    product_id = models.ManyToManyField(Product)