import os
import datetime
import shutil
import uuid
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.sessions.models import Session
from django.utils import timezone



def index(request):
    return render(request, 'index.html', locals())