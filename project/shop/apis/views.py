from rest_framework.decorators import APIView
from rest_framework.response import Response
from shop.apis.serializers import *
from rest_framework import status
class ShopAPIView(APIView):

    def post(self, request):

        serializer = ShopSerializer(data = request.data)
        # to validate the serializer
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_201_CREATED)
        else:
            # if serializer is not valid returns what the problem is
            return Response(data=serializer.errors)
        