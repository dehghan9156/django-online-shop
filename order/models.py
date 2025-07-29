from django.db import models
from django.contrib.auth import get_user_model
from product.models import * 

User = get_user_model()



RELEVANCE_CHOICES = (
    ("Waiting",("waiting")),
    ("Paid",("paid")),
    ("Sent",("sent")),
    ("Delivered",("delivered")),
    ("Canceled",("canceled")),
)



class HeaderFactor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(choices=RELEVANCE_CHOICES,max_length=250)


class Factor(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    header_factor = models.ForeignKey(HeaderFactor,on_delete=models.CASCADE)