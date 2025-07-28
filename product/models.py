from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='product/',blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    color = models.CharField(blank=True,null=True)
    quantity = models.IntegerField()
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
