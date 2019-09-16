# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Destination

def home(request):

    

    dests=Destination.objects.all()
    return render(request, 'index.html',{'dests':dests})

