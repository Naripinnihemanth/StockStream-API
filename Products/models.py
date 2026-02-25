from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class category(models.Model):
    id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.title


class ProductModel(models.Model):
    id=models.BigAutoField(primary_key=True,auto_created=True)
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    category=models.ForeignKey(category,on_delete=models.CASCADE,name="category")
    price=models.DecimalField(decimal_places=2,max_digits=6)
    image=models.ImageField(upload_to="product_images/",null=False)
    currency=models.CharField(max_length=10)
    stock=models.IntegerField()
    created_at=models.DateTimeField(default=timezone.now)
    descount=models.IntegerField(default=0)
    ratting=models.IntegerField(default=3)
    color=models.CharField(max_length=20,default="")
    brand=models.CharField(max_length=30,default="")
    slug=models.CharField(max_length=50,default="")
    views=models.IntegerField(default=0)
    def __str__(self):
        return self.title

class cartModel(models.Model):
    auther=models.ForeignKey(User,on_delete=models.CASCADE)
    item_id=models.IntegerField()
    item_title=models.CharField(max_length=200)
    item_color=models.CharField(max_length=100)
    item_image=models.CharField(max_length=1000)
    quantity=models.IntegerField(default=1)
    item_price=models.IntegerField()
    item_descount=models.IntegerField(default=0)

    def __str__(self):
        return self.item_title