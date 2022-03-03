from rest_framework import serializers
from .models import Provider, PolygonZone

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('__all__')


class PolygonSerializer(serializers.ModelSerializer):

    class Meta:
        model = PolygonZone
        fields = ('__all__')


class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = PolygonZone
        fields = ['provider','name', 'price']