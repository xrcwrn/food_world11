from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated 

from .models import Item
from .serializer import ItemSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getItems(request):
   app = Item.objects.all()
   serializer = ItemSerializer(app, many=True)
   return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getItem(request, id=None):
            item = Item.objects.get(id=id)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
       
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def postItem(request):
   serializer = ItemSerializer(data=request.data)
   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
   else:
      return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes((IsAuthenticated, ))
def update(request, id=None):
      item = Item.objects.get(id=id)
      serializer = ItemSerializer(item, data=request.data, partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response({"status": "success", "data": serializer.data})
      else:
         return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def delete(request, id=None):
      item = Item.objects.get(id=id)
      serializer = ItemSerializer(item, data=request.data, partial=True)
      item.delete()
      return Response({"status": "success", "data": "Item Deleted"})        




