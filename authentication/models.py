from django.db import models
from django.contrib.auth.models import User
import datetime
class custemUserModel(models.Model):
    auther=models.ForeignKey(User,on_delete=models.CASCADE,related_name="personal_data")
    profile=models.ImageField(upload_to="profiles/",default="../media/constents/unknown.jpeg")
    bio=models.TextField(max_length=100,default="")
    def __str__(self):
        return self.auther.username
    
class historyModel(models.Model):
    auther=models.ForeignKey(User,on_delete=models.CASCADE,related_name="history")
    product_id=models.IntegerField(default=0)
    title=models.CharField(max_length=50)
    category=models.TextField(max_length=50)
    price=models.DecimalField(decimal_places=2,max_digits=6)
    image=models.CharField(max_length=200,default="../media/constents/unknown.jpeg")
    def __str__(self):
        return self.title
    
class addreddModel(models.Model):
    auther=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    primary_nummber=models.IntegerField()
    alter_nummber=models.IntegerField(null=True)
    address_line_one=models.CharField(max_length=500)
    address_line_two=models.CharField(max_length=500,null=True,blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    Country=models.CharField(max_length=50,default="india")
    pin_code=models.IntegerField(default=0)
    add_type=models.CharField(max_length=10,default="home")
    default=models.BooleanField()
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.auther.username


class UserOrdersModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    auther = models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")
    payment_status=models.CharField(max_length=50,choices=[ ("pending", "Pending"),
            ("accepted", "Accepted"),
            ("failed", "Failed"),
            ("refunded", "Refunded"),
            ("cancelled", "Cancelled"),],default="pending")
    payment_id=models.CharField(max_length=300,null=True,blank=True)
    payment_type=models.CharField(max_length=100)
    totel_amount=models.IntegerField(null=False,default=0)
    message=models.CharField(max_length=300,default="",null=True)
    product_id=models.IntegerField(null=False)
    quantity=models.IntegerField(default=1)
    address=models.ForeignKey(addreddModel,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.id)
# class AllOrderedProducts(models.Model):
#     order=models.ForeignKey(UserOrdersModel, on_delete=models.CASCADE, related_name="products",null=True)
#     product_image=models.CharField(max_length=300)

#     def __str__(self):
#         return str(self.product_id)