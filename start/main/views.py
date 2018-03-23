 # -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse,JsonResponse

def index(request):

    return render(request,'login.html')