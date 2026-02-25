from rest_framework import serializers
from .models import *

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields=["id","title","description","category","price","image","currency","stock","created_at","descount","ratting","color","brand","slug","views"]
        extra_kwargs={
            "created_at":{
                "read_only":True
            }
        }

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields="__all__"

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model=cartModel
        fields="__all__"
        extra_kwargs={
            "auther":{
                "read_only":True
            }
        }

class quantitySerializer(serializers.ModelSerializer):
    class Meta:
        model=cartModel
        fields=["id","quantity","item_price"]


class incSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields=["views"]