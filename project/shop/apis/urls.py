from django.urls import path

from shop.apis.views import *

urlpatterns = [
    # urls to the views
    path("create-shop/", ShopAPIView.as_view()),
]
