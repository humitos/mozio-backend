from django.conf.urls import url, include
from rest_framework import routers
from serviceareas import views

router = routers.DefaultRouter()
router.register(r'provider', views.ProviderViewSet)
router.register(r'servicearea', views.ServiceAreaViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]