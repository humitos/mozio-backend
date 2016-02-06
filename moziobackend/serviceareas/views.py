from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from serviceareas.models import Provider, ServiceArea
from serviceareas.serializers import ProviderSerializer, ServiceAreaSerializer, ServiceAreaCreateSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    Returns all the Provider ordered by name
    """

    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializer
    http_method_names = ['get', 'post', 'update', 'delete']


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    Returns all the ServiceArea ordered by name
    """

    queryset = ServiceArea.objects.all().order_by('name')
    serializer_class = ServiceAreaCreateSerializer
    partial = True
    http_method_names = ['get', 'post', 'update', 'delete']


class ServiceAreaForPoint(APIView):
    """
    Given a POINT(lng, lat) it will return all the ServiceArea working
    on that specific POINT
    """

    def get(self, request, lat, lng, format=None):
        point = Point(float(lng), float(lat))
        serviceareas = ServiceArea.objects.filter(polygon__contains=point)
        serializer = ServiceAreaSerializer(serviceareas, many=True)
        return Response(serializer.data)
