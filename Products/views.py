from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.parsers import MultiPartParser,FormParser
from django.shortcuts import get_object_or_404

class productsView(generics.ListCreateAPIView):
    queryset=ProductModel.objects.all()
    serializer_class=productSerializer
    permission_classes=[AllowAny]

class detailsView(generics.RetrieveAPIView):
    queryset=ProductModel.objects.all()
    serializer_class=productSerializer
    permission_classes=[AllowAny]

class searchView(generics.ListAPIView):
    serializer_class=productSerializer
    permission_classes=[AllowAny]
    def get_queryset(self):
        word=self.kwargs["pk"]
        categ=get_object_or_404(category,title=word)
        products=ProductModel.objects.filter(category=categ)
        return products
    
class categoryView(generics.ListAPIView):
    queryset=category.objects.all()
    serializer_class=categorySerializer
    permission_classes=[AllowAny]

class trendingView(generics.ListAPIView):
    serializer_class= productSerializer
    permission_classes=[AllowAny]


    def get_queryset(self):

        products=ProductModel.objects.filter(views__gt=500)

        return products
    
class setCartView(generics.CreateAPIView):
    serializer_class=cartSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):

        if(serializer.is_valid()):
            serializer.save(auther=self.request.user)
    
class getCartView(generics.ListAPIView):
    serializer_class=cartSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return cartModel.objects.filter(auther=self.request.user)
    
class setQuantityView(generics.RetrieveUpdateAPIView):

    queryset=cartModel.objects.all()
    serializer_class=quantitySerializer
    permission_classes=[AllowAny]



class deleteCartView(generics.DestroyAPIView):
    queryset=cartModel.objects.all()
    serializer_class=cartSerializer
    permission_classes=[IsAuthenticated]

class incView(generics.RetrieveUpdateAPIView):
    queryset=ProductModel.objects.all()
    serializer_class=incSerializer
    permission_classes=[AllowAny]
    