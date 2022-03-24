from django.shortcuts import render

from django.http import HttpResponse

def plug(request):
    return HttpResponse('plug')