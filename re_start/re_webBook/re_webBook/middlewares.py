from django.contrib.auth import authenticate, login
from django.http import HttpResponse

class AutoLogin:
    """повторение"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            user = authenticate(username='adminus', password='adminus')
            login(request, user)
        response =self.get_response(request)
        return response



























#
# def auto_login(get_response):
#     def middleware(request):
#         if not request.user.is_authenticated:
#             user = authenticate(username='adminus', password='adminus')
#             login(request, user)
#         # return HttpResponse('test global plug')
#         return get_response(request)
#     return middleware


# class AutoLogin:
#     def __init__(self,get_response):
#         """запускается при запуске сервера"""
#         self.get_response = get_response
#
#     def __call__(self, request):
#         """ запускается при каждом запросе """
#         if not request.user.is_authenticated:
#             user = authenticate(username='adminus', password='adminus')
#             login(request, user)
#
#         response = self.get_response(request)
#         return response
#         # return HttpResponse('test global plug')