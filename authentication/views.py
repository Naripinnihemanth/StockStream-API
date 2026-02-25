from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser
from Products.models import *
from Products.serializers import *
from .ml_model import RecommendationML

ml_engine = RecommendationML()
ml_engine.train()

class authView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer
    permission_classes=[AllowAny]


class profileView(generics.CreateAPIView):
    queryset=custemUserModel.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


    def perform_create(self, serializer):
        custemUserModel.objects.filter(
            auther=self.request.user
        ).delete()

        if serializer.is_valid():
            serializer.save(auther=self.request.user)
        else:
            print(serializer.errors)

class getUser(generics.ListAPIView):
    serializer_class=userSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user.id
        data=User.objects.filter(id=user)
        return data

class getProfile(generics.ListAPIView):
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return custemUserModel.objects.filter(auther=self.request.user)
    
class setHistory(generics.ListCreateAPIView):
    queryset=historyModel.objects.all()
    serializer_class=historySerialiser
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        historyModel.objects.filter(
            product_id=self.request.data.get("product_id"),auther=self.request.user
        ).delete()
        # prod_id=self.kwargs["id"]
        # print(prod_id)
        # product=productModel.objects.get(id=prod_id)
        
        # created_product=historyModel.objects.create(auther=self.request.user,product_id=product.id,title=product.title,category=product.category,price=product.price,image=product.image)

        # return created_product
        if serializer.is_valid():
            serializer.save(auther=self.request.user)
        else:
            print(serializer.errors)

class getHistory(generics.ListAPIView):
    serializer_class=historySerialiser
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        history_products=historyModel.objects.filter(auther=self.request.user)


        return history_products
    
class deleteHistory(generics.DestroyAPIView):
    queryset=historyModel.objects.all()
    serializer_class=historySerialiser
    permission_classes=[IsAuthenticated]

class RecommendProducts(generics.ListAPIView):
    serializer_class = productSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ml_engine.recommend(self.request.user)


class SetAddressView(generics.CreateAPIView):
    queryset=addreddModel.objects.all()
    serializer_class=addressSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user= self.request.user
        if serializer.is_valid():
            serializer.save(auther=user)

class getAddres(generics.ListAPIView):
    serializer_class = addressSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        return addreddModel.objects.filter(auther=self.request.user)
    

class setDefaultAddress(generics.RetrieveUpdateAPIView):
    queryset=addreddModel.objects.all()
    serializer_class=setDefaultAddressSerializer 
    permission_classes=[AllowAny]

    def perform_update(self, serializer):
        addreddModel.objects.filter(auther=self.request.user,default=True).update(default=False)
        serializer.save()

class getDefaultAddress(generics.ListAPIView):
    serializer_class= addressSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return addreddModel.objects.filter(auther=self.request.user,default=True)

class getSingleAddress(generics.RetrieveAPIView):
    queryset=addreddModel.objects.all()
    serializer_class=addressSerializer
    permission_classes=[IsAuthenticated]


class setOrder(generics.ListCreateAPIView):
    queryset=UserOrdersModel.objects.all()
    serializer_class=orderSerializer
    permission_classes=[AllowAny]

    def perform_create(self, serializer):
        user_address=get_object_or_404(addreddModel,auther=self.request.user,default=True)
        if serializer.is_valid():
            serializer.save(auther=self.request.user,address=user_address)


class getOrders(generics.ListAPIView):
    serializer_class=orderSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return UserOrdersModel.objects.filter(auther=self.request.user)