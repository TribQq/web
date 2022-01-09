from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from main.models import Bb
from .serializers import *


@api_view(['GET'])
def bbs(request): # Контроллер, который будет выдавать список объявлений,
    if request.method == 'GET':
        bbs = Bb.objects.filter(is_active=True)[:10]
        serializer = BbSerializer(bbs, many=True)
        return Response(serializer.data)


class BbDetailView(RetrieveAPIView): # Контроллер, выдающий сведения о выбранном объявлении,
    queryset = Bb.objects.filter(is_active=True)
    serializer_class = BbDetailSerializer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,)) # разрешим добавлять комментарии только зарегистрированным пользователям, а просматривать их, напротив, позволим всем пометили контроллер декоратором perrnission _ classes ( ) , в котором указали класс разграничения доступа I sAuthenti catedOrReadOnly.
def comments(request, pk):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    else:
        comments = Comment.objects.filter(is_active=True, bb=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)