from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=custemUserModel
        fields=["auther","profile","bio"]
        extra_kwargs={
            "auther":{
                "read_only":True
            }
        }

class userSerializer(serializers.ModelSerializer):


    class Meta:
        model=User
        fields=["username","password","first_name","last_name","email","last_login"]
        extra_kwargs={
            "password":{
                "write_only":True
            },
            "last_login":{
                "read_only":True
            },
        }

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    
class historySerialiser(serializers.ModelSerializer):
    class Meta:
        model=historyModel
        fields=["id","auther","product_id","title","category","price","image"]
        extra_kwargs={
            "auther":{
                "read_only":True
            }
        }
        

class addressSerializer(serializers.ModelSerializer):
    class Meta:
        model=addreddModel
        fields=["id","auther","first_name","last_name","primary_nummber","alter_nummber","address_line_one","address_line_two","city","state","Country","pin_code","default","create_at"]
        extra_kwargs={
            "auther":{
                "read_only":True
            }
        }

class setDefaultAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=addreddModel
        fields=["default"]


# class orderedProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=AllOrderedProducts
#         fields="__all__"
#         extra_kwargs={
#             "order":{
#                 "read_only":True
#             }
#         }


class orderSerializer(serializers.ModelSerializer):

    # products=orderedProductSerializer(many=True,read_only=True)

    # upload_ids=serializers.ListField(
    #     child=serializers.IntegerField(),
    #     write_only=True
    # )

    # upload_images=serializers.ListField(
    #     child=serializers.CharField(),
    #     write_only=True
    # )

    # upload_quantity=serializers.ListField(
    #     child=serializers.IntegerField(),
    #     write_only=True
    # )

    class Meta:
        model=UserOrdersModel
        fields=["id","auther","payment_status","payment_id","payment_type","product_id","quantity","totel_amount","message","address"]
        extra_kwargs={
            "auther":{
                "read_only":True
            },
            "payment_status":{
                "read_only":True
            },
            "message":{
                "read_only":True
            },
            "address":{
                "read_only":True
            }
        }

    # def create(self, validated_data):

    #     ids=validated_data.pop("upload_ids")
    #     images=validated_data.pop("upload_images")
    #     quntities=validated_data.pop("upload_quantity")

    #     item=UserOrdersModel.objects.create(**validated_data)
    #     for i in range(len(ids)):
    #         AllOrderedProducts.objects.create(order=item,product_id=ids[i],product_image=images[i],quantity=quntities[i])
    #     return item