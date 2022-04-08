from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse


def page_not_found_view(request, exception):
    """ redirect to 404 handler """
    return redirect(reverse('about_me:handler_404', kwargs={}))

