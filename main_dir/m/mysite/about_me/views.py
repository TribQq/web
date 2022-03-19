from django.shortcuts import render

def about_main(request):
    return render(request, 'about_me_main.html')