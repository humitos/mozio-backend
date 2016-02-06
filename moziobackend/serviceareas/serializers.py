from rest_framework import serializers
from serviceareas.models import Provider, ServiceArea
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', 'email', 'phone', 'language', 'currency')


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    provider = ProviderSerializer()

    class Meta:
        model = ServiceArea
        geo_field = 'polygon'
        fields = ('name', 'price', 'polygon', 'provider')
