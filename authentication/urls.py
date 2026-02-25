from django.urls import path
from .views import *
urlpatterns=[
    path("register/",authView.as_view(),name="register"),
    path("setProfile/",profileView.as_view(),name="setProfile"),
    path("getProfile/",getProfile.as_view(),name="getProfile"),
    path("sethistory/",setHistory.as_view(),name="sethistory"),
    path("gethistory/",getHistory.as_view(),name="gethistory"),
    path("deletehistory/<int:pk>/",deleteHistory.as_view(),name="delethistory"),
    path("recomendations/",RecommendProducts.as_view(),name="recomendations"),
    path("setaddress/",SetAddressView.as_view(),name="setaddress"),
    path("getaddress/",getAddres.as_view(),name="getaddress"),
    path("getsingleaddress/<int:pk>/",getSingleAddress.as_view(),name="getsingleaddress"),
    path("setdefaultaddress/<int:pk>/",setDefaultAddress.as_view(),name="setdefalutaddress"),
    path("getdefaultaddress/",getDefaultAddress.as_view(),name="getdefalutaddress"),
    path("getuser/",getUser.as_view(),name="getuser"),
    path("setorder/",setOrder.as_view(),name="setorder"),
    path("getorder/",getOrders.as_view(),name="getorder"),
]