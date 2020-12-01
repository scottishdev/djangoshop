from rest_framework import serializers
from shop.models import *

# serializer for shop
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = "__all__"