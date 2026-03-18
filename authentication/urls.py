from django.urls import path
from .views import *
urlpatterns=[
    path("",authView.as_view(),name="register"),
    # path("api/setProfile/",profileView.as_view(),name="setProfile"),
    # path("api/getProfile/",getProfile.as_view(),name="getProfile"),
    path("api/sethistory/",setHistory.as_view(),name="sethistory"),
    path("api/gethistory/",getHistory.as_view(),name="gethistory"),
    path("api/deletehistory/<int:pk>/",deleteHistory.as_view(),name="delethistory"),
    path("api/recomendations/",RecommendProducts.as_view(),name="recomendations"),
    path("api/setaddress/",SetAddressView.as_view(),name="setaddress"),
    path("api/getaddress/",getAddres.as_view(),name="getaddress"),
    path("api/getsingleaddress/<int:pk>/",getSingleAddress.as_view(),name="getsingleaddress"),
    path("api/setdefaultaddress/<int:pk>/",setDefaultAddress.as_view(),name="setdefalutaddress"),
    path("api/getdefaultaddress/",getDefaultAddress.as_view(),name="getdefalutaddress"),
    path("api/getuser/",getUser.as_view(),name="getuser"),
    path("api/setorder/",setOrder.as_view(),name="setorder"),
    path("api/getorder/",getOrders.as_view(),name="getorder"),
]