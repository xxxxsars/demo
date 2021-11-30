# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url, include
from api.views import *

urlpatterns = [
    url("save_image/$", save_image),
]