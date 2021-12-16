from django.test import TestCase
from django.urls import resolve
from rest_framework import status
from demo.views import index


class TestIndexView(TestCase):

    def test_resolve_to_index_page(self):
        found = resolve('/')
        # check function name is equal
        self.assertEqual(found.func.__name__, index.__name__)

    def test_get_index_page(self):
        """
        Ensure we can website index page.
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)