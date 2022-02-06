from django.contrib.auth import authenticate, login


def auto_login(get_response): # с помошью этой штуки можно залочить или создать любую иерархию , пример ниже
    def middleware(request):
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