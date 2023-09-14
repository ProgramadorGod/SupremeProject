from django.db import models

# Create your models here.

class Category_Prod(models.Model):
    Name = models.CharField(max_length=40)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.FloatField(max_length=25)
    Image = models.ImageField(upload_to='Store', null=True, blank=True)
    Categorie = models.ForeignKey(Category_Prod,on_delete=models.CASCADE)
    Disponibility = models.BooleanField(default=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name =  "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.Name