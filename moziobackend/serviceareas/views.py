from rest_framework import viewsets
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


# class ServiceAreaForPoint():

    
