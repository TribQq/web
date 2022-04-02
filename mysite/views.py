from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse


def page_not_found_view(request, exception):
    # return HttpResponse('plug')
    # return render(request, '404.html', status=404)
    # return render(request, '404.html')
    return redirect(reverse('about_me:handler_404', kwargs={}))
