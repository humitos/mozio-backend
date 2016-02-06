from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from serviceareas.models import Provider


class ProviderTests(APITestCase):
    def test_create_no_login(self):
        url = reverse('provider-list')
        data = {
            'name': 'Lima Delivery'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Provider.objects.count(), 0)
