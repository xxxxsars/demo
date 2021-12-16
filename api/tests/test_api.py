from datetime import datetime, timezone, timedelta

import json

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Predict_log

class AccountTests(APITestCase):
    def setUp(self):

        self.now_time = datetime.now(timezone(timedelta(hours=+8)))
        self.product_id = "1"
        self.raw_image = "base64_img_1"
        self.gray_image = "gray_base64_img_1"

        Predict_log.objects.create(production_id=self.product_id,
                                   raw_image=self.raw_image,
                                   gray_image=self.gray_image,
                                   created_at=self.now_time)
    def test_get_predict(self):
        """
        Ensure we can get predict log result.
        """
        url = reverse('predict-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_predict_detail(self):
        """
        Ensure we can get predict log result with the production id.
        """
        url = reverse('predict-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {"production_id":self.product_id,"raw_image":self.raw_image,"gray_image":self.gray_image,"created_at": self.now_time.isoformat()})






