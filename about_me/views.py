# from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def about_main(request):
    return render(request, 'about_me_main.html')


def alt_about_me(request):
    return render(request, 'alt_about_me.html')


def handler_404(request):
    """ page for 404 error"""
    return render(request, 'handlers/404.html')