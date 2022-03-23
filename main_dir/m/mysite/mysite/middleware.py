from django.contrib.auth import authenticate, login


class BookshelfAutoLogin:
    """middleware для авто логина при исп bookshelf, можно было просто прикрутить деркоратор к прогрессу,но  концепт c middleware мне понравился больше)"""
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        if (str(request)[:31] =="<WSGIRequest: GET '/bookshelf/'"
                and not request.user.is_authenticated):
            user = authenticate(username='visitor', password='visitor')
            login(request, user)
        response = self._get_response(request)
        return response


