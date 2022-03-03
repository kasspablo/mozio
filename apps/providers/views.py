from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.decorators import api_view
from shapely.geometry import Polygon, Point
from .serializers import (
    ProviderSerializer, 
    PolygonSerializer,
    ZoneSerializer
)
from .models import Provider, PolygonZone

# Create your views here.

class ProvidersList(ListAPIView):
    """
    List all providers
    """
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

class ProviderList(ListCreateAPIView):
    """
    Create a new provider
    """
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

class ProviderDetail(RetrieveUpdateDestroyAPIView):
    """
    Recover, Update and Delete an existing provider
    """
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class PolygonList(ListCreateAPIView):
    """
    Create a new zone
    """
    serializer_class = PolygonSerializer
    queryset = PolygonZone.objects.all()

class PolygonDetail(RetrieveUpdateDestroyAPIView):
    """
    Recover, Update and Delete an existing zone
    """
    serializer_class = PolygonSerializer
    queryset = PolygonZone.objects.all()


class ZoneList(ListAPIView):
    """
    Find a provider in the area, sorting by price, id_provider and name
    """
    serializer_class = ZoneSerializer
    
    def get_queryset(self):
        lat = self.request.GET.get('lat', None)
        lng = self.request.GET.get('lng', None)

        if (lat is None) or (lng is None):
            return []

        queryset = PolygonZone.objects.all().order_by('price', 'provider', 'name')
        providers = []
        point = Point(float(lat), float(lng))
        for provider in queryset:
            e = eval(provider.polygon)
            if Polygon(e).covers(point):
                providers.append(provider)
        return providers