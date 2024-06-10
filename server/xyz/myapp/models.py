from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_code = models.IntegerField(unique=True)
    description = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)
    details = models.CharField(max_length=255, null=True, blank=True)
    stockquantity = models.IntegerField(default=0) 

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.description
