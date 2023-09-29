from django.db import models


from django.contrib.auth.models import User
from Store.models import Product

# Create your models here.
class ProductRelation(models.Model):
    user = models.ForeignKey(User, null='True', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null='True', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)