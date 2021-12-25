from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

from .models import *

from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy

def index(request):
    # template = loader.get_template('bboard/index.html') #загружаем шаблон
    bbs = Bb.objects.all()
    # context = {'bbs':bbs} #дикт ключ : обьекты с их подобьектами (п:obj-дом(подобьект(title,text,price))
    # return HttpResponse(template.render(context,request)) # рендерим шаблон на основе данных и возвращаем
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics':rubrics}
    return render(request,'bboard/index.html',context)

def by_rubric(request,rubric_id): #reques - указание дальнейшего маршрута
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs ,'rubrics':rubrics,'current_rubric':current_rubric}
    return render(request,'bboard/by_rubric.html',context)

def index_1(request):
    return HttpResponse('12345')

class BBCreateView(CreateView): # выскоуровневый контроллер-класс
    #производный от базового класса который уже настроен в жанге из коробки
    template_name='bboard/create.html' # путь к файлу шаблона, создающего страницу с формой;
    form_class =BbForm #—ссылка на класс формы, связанной с моделью;
    succes_url=reverse_lazy('index') # интернет-адрес для перенаправления после(нэйм url pattern`a)
    #возможно ошибка!!!!!!!!!!!!!!!!!!

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context