from rest_framework import serializers
from serviceareas.models import Provider, ServiceArea
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', 'email', 'phone', 'language', 'currency')


class ServiceAreaSerializer(serializers.HyperlinkedModelSerializer):
    provider = serializers.StringRelatedField()

    class Meta:
        model = ServiceArea
        fields = ('name', 'provider', 'price')


class ServiceAreaCreateSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ServiceArea
        geo_field = 'polygon'
        fields = ('name', 'provider', 'polygon', 'price')
