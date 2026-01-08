from django.shortcuts import render
from properties.serializer import PropertySerializer
from rest_framework import views, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Property


# Create your views here.
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]

class PropertiesSaleViewSet(views.APIView):
   permission_classes = [AllowAny]
   def get(self, request, *args, **kwargs):
       sales =[choice[0] for choice in Property.SALE_CHOICES]
       return Response(sales)


class PropertiesHomeViewSet(views.APIView):
   permission_classes = [AllowAny]
   def get(self, request, *args, **kwargs):
       homes =[choice[0] for choice in Property.HOME_CHOICES]
       return Response(homes)
   

class PropertiesParkingViewSet(views.APIView):
   permission_classes = [AllowAny]
   def get(self, request, *args, **kwargs):
       parkings =[choice[0] for choice in Property.PARKING_CHOICES]
       return Response(parkings)
   

