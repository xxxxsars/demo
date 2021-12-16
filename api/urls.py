# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url, include
from api.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', PredictLogViewSet, basename='predict')

urlpatterns = [
    url("save_image/$", save_image),
    url(r'^predict_log/', include(router.urls))
]