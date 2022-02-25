from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer
from .serializers import *


@api_view
def view_customers_list(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = Customer.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 10) # Если это запрос GET, метод разбивает данные на страницы с помощью Django Paginator и возвращает первую страницу данных после сериализации, количество доступных клиентов, количество доступных страниц и ссылки на предыдущие и последующие страницы. Paginator — это встроенный класс Django, выполняющий разбивку списка данных на страницы и предоставляющий методы доступа к элементам на каждой странице.
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = CustomerSerializer(data, context={'request': request}, many=True)
        if data.has_next():  # custom pagination method (not cPython)
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data, 'count': paginator.count,
                         'numpages': paginator.num_pages,
                         'nextlink': '/api/customers/?page=' + str(nextPage),
                         'prevlink': '/api/customers/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # сохраняем data сериалайзер`a если он валиден
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # if not valid


@api_view(['GET', 'PUT', 'DELETE']) # API, который может принимать запросы GET, PUT и DELETE.
def view_customers_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist: # ловим ошибку 'если не существет'
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer, context={'request': request}) #  сериализация данных клиента и их отправка
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data, # need check data.request для понимания
                                        context={'request': request}) # создает сериализатор для новых данных клиента
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # Response с обновленными данными клиента.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) #? # объект Response, не содержащий никаких данных.


