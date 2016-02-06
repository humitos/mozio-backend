from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from serviceareas.models import Provider, ServiceArea
from serviceareas.serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = ServiceArea.objects.all().order_by('name')
    serializer_class = ServiceAreaSerializer


class ServiceAreaForPoint(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, lat, lng, format=None):
        point = Point(float(lng), float(lat))
        serviceareas = ServiceArea.objects.filter(polygon__contains=point)
        serializer = ServiceAreaSerializer(serviceareas, many=True)
        return Response(serializer.data)
