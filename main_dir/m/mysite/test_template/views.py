from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

def baic_template(request):
    return render(request, 'layout/bookshelf_basic.html')


def template_with_text(request):
    return render(request, 'main_note.html')