# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'home.html',{'name':'Suyash'})

def add(request):
    val1 = request.POST["num1"]
    val2 = request.POST["num2"]
    res = int(val1) + int(val2)
    return render(request, 'result.html',{'result':res})