from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView,CreateView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import AdvUser
from .forms import ChangeUserInfoForm,RegisterUserForm


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
    # LoginRequiredМixin- запрещет доступ к контроллеру гостям, и примесь SuccessMessageMixin n,- для вывода всплывающих сообщений об успешном выполнении операции
    model = AdvUser  # использует модель..
    template_name = 'main/change_user_info.html' #адресс
    form_class = ChangeUserInfoForm # использует форму
    success_url = reverse_lazy('main:profile') #после юза перенаправляет на
    success_message = 'Данные изменены'
    def setup(self, request, *args, **kwargs):
        # наилучшее место для получения ключа текущего пользователя - метод setup ( ) , наследуемый всеми контроллерами-классами от их общего суперкласса
        # View. Этот метод выполняется в самом начале исполнения контроллера-класса и получает объект запроса в качестве одного из параметров.
        self.user_id = request.user.pk # онтроллера-класса и получает объект запроса в качестве одного из параметров. В переопределенном методе setup () мы извлечем ключ пользователя и сохраним его в атрибуте user _ id.
        return super().setup(request, *args, **kwargs)
        # стр 610
    def get_object(self, queryset = None):# Извлечение исправляемой записи выполняем в методе get _ obj ect ( )
        # который контроллер-класс унаследовал от примеси S ingleObj ectMixin
        if not queryset: # В переопределенном методе сначала учитываем тот момент, что набор записей, из которого следует извлечь искомую запись, может быть передан методу с параметром queryset, а может
        #  быть и не передан - в этом случае набор записей следует получить вызовом метода get _ queryset ( ) .
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id) # непосредственно ищем запись, представляющую текущего пользователя.


class RegisterUserView(CreateView): #контроллер-класс регистр пользовател стр 615
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')

class RegisterDoneView(TemplateView): # Контроллер, который выведет сообщение об успешной регистрации w и, в силу его исключительной простоты, станет производным от класса TemplateView
    template_name = 'main/register_done.html'
