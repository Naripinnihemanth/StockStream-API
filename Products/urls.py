from django.urls import path
from .views import *
urlpatterns=[
    path("upload/",productsView.as_view(),name="uploadProducts"),
    path("getProduct/<int:pk>/",detailsView.as_view(),name="productDetails"),
    path("search/<str:pk>/",searchView.as_view(),name="search"),
    path("getcategory/",categoryView.as_view(),name="categories"),
    path("trending/",trendingView.as_view(),name="trending"),
    path("setcart/",setCartView.as_view(),name="cart"),
    path("getcart/",getCartView.as_view(),name="getcart"),
    path("setquantity/<int:pk>/",setQuantityView.as_view(),name="setquantity"),
    path("deletecart/<int:pk>/",deleteCartView.as_view(),name="deletecart"),
    path("viewsincreas/<int:pk>/",incView.as_view(),name="increaseviews"),
]