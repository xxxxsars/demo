from django.test import TestCase
from django.urls import reverse
from api.models import Predict_log
import json


class ApiTestCase(TestCase):
    def setUp(self):
        print(2)
        Predict_log.objects.create(production_id="1",
                                   raw_image="base64_img_1",
                                   gray_image="gray_base64_img_1")

    def test_predict_log_data(self):
        """
        Ensure we can create predict log to database.
        """
        self.assertEqual(Predict_log.objects.count(), 1)
        self.assertEqual(Predict_log.objects.get().raw_image, 'base64_img_1')



