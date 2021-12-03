from django.shortcuts import render,redirect
from .models import Tabli4ka
from .forms import Tabli4kaForm


def index_x(request):# обработчик мэн пэйджа
    tasks = Tabli4ka.objects.order_by('-id') # реверсивная сортировка по ид + срез можно например [:1]
    return render(request , 'main_application/index.html', {'title': 'main page site' , 'tasks': tasks})

def about_t(request): #обработчик about page
    return  render(request , 'main_application/about.html')        #HttpResponse("<h4> about sus </h4>") # не самая удобная функц т.к в неё особо файл не запихаешь

def create_task(request):
    error = ''
    if request.method == 'POST': #если метод пост то мы не просто перенаправляем, а уже берём и работаем с данными
        form = Tabli4kaForm(request.POST) #уже наполненный данными от пользователя обьект
        if form.is_valid(): #если данные корректны
            form.save() # сэве (в бд)
            return redirect('home_page') #перенапрявлем на хоум страницу
        else:
            error = 'text in form error'

    form = Tabli4kaForm() #обьект созданный на основе класса
    context = {
        'form_m' : form,
        'error_r' : error # либо пустая(изначально, Либо текст с ошибкой)
    }
    return render(request, 'main_application/new_task.html' ,context) #без добавления , context не передаёт значения дальше по конееверу...