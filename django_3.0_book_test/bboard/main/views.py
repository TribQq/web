from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request,'main/index.html')


def other_page(request,page): # получает запрашиваему страницу от вызываеющего метода urls (тот что на уровне приложения)
    try:
        template = get_template('main/'+ page +'.html')
    except TemplateDoesNotExist: #условие для принятия возможной ошибки генерируемой get_template() и скормит 404 протоколу
        raise Http404
    return HttpResponse(template.render(request=request))

class BBLoginView(LoginView): #контроллер-класс (подкласс втроенного)
    template_name = 'main/login.html'
@login_required    # декоратор - ограничитель(чекер регистрации юзера)
def profile(request):
    return render(request, 'main/profile.html')

class BBLogoutView(LoginRequiredMixin, LogoutView): #LoginRequiredMixin - чек регистрации + чек входа
    template_name = 'main/logout.html'




