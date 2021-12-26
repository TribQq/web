from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import AdvUser
from .forms import ChangeUserInfoForm


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

class BBLogoutView(LoginRequiredMixin, LogoutView): # LoginRequiredMixin - чек регистрации + чек входа
    template_name = 'main/logout.html'


class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль изменён'

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser  #использует модель..
    template_name = 'main/change_user_info.html' #адресс
    form_class = ChangeUserInfoForm # использует форму
    success_url = reverse_lazy('main:profile') #после юза перенаправляет на
    success_message = 'Данные изменены'
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk # получает ключ модели текущего пользователя
        return super().setup(request, *args, **kwargs) #В переопределенном методе setup () мы извлечем ключ пользователя и сохраним его в атрибуте user _ id
        # стр 610
    def get_object(self, queryset = None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)



