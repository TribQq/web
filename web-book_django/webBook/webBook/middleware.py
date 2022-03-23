from django.contrib.auth import authenticate, login


def auto_login(get_response): # с помошью этой штуки можно залочить или создать любую иерархию , пример ниже
    def middleware(request):
        print((str(request)+' ==request\n')*10)
        if not request.user.is_authenticated:
            user = authenticate(username='adminus', password='adminus') # так же можно настроить под любого пользователя например под демо режим демо юзера
            login(request, user)
        return get_response(request)
    return middleware


# from django.http import HttpResponse
# def auto_login(get_response): #  заменить любую юрлху на уровне запроса в просто текст респонса 15"45(2)
#     def middleware(request):
#         return HttpResponse('HI its test')
#         response = get_response(request)
#         return response
#     return middleware


# class BookshelfAutoLogin:
#     """middleware для авто логина при исп bookshelf, можно было просто прикрутить деркоратор к прогрессу,но  концепт c middleware мне понравился больше)"""
#     def __init__(self, get_response):
#         self._get_response = get_response
#
#     def __call__(self, request):
#         print('start middleare')
#         print((str(request)+' ==request\n')*1)
#         if not request.user.is_authenticated:
#             user = authenticate(username='adminus', password='adminus')
#             login(request, user)
#         response = self._get_response(request)
#         # print('after view logic')
#         return response

