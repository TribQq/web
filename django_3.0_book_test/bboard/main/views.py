#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.signing import BadSignature


from .models import AdvUser
from .forms import ChangeUserInfoForm,RegisterUserForm
from .utilities import signer

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
    def get_object(self, queryset=None):# Извлечение исправляемой записи выполняем в методе get _ obj ect ( )
        # который контроллер-класс унаследовал от примеси S ingleObj ectMixin
        if not queryset: # В переопределенном методе сначала учитываем тот момент, что набор записей, из которого следует извлечь искомую запись, может быть передан методу с параметром queryset, а может
        #  быть и не передан - в этом случае набор записей следует получить вызовом метода get _ queryset ( ) .
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id) # непосредственно ищем запись, представляющую текущего пользователя.


class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль изменён'


class BBPasswordChangeViewFromAdmin(PasswordChangeView):
    pass

class RegisterUserView(CreateView): #контроллер-класс регистр пользовател стр 615
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')

class RegisterDoneView(TemplateView): # Контроллер, который выведет сообщение об успешной регистрации w и, в силу его исключительной простоты, станет производным от класса TemplateView
    template_name = 'main/register_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign) #Подписанный идентификатор пользователя, передаваемый в составе интернетадреса, получаем с параметром sign. Далее извлекаем из него имя пользователя,
    except BadSignature:
        return render(request, 'main/bad_signature.html') # перенаправление в случае неудачи
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user_is_activated.html' # в случае уже активиров
    else:
        template = 'main/activation_done.html' # актив завершен
        user.is_active = True #  делаем его активным, присвоив значения тrue
        user.is_activated = True  #делаем его активным, присвоив значения тrue
        user.save()
    return render(request, template)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')

    def setup(self,request, *args, **kwargs):
        self.user_id = request.user.pk #тоже что и в ChangeUserInfoView: взяли ключ юзера
        return super().setup(request, *args, **kwargs) #  В переопределенном методе setup () сохранили ключ текущего пользователя

    def post(self,request, *args, **kwargs): #Перед удалением текущего пользователя необходимо выполнить выход, что мы и сделали в переопределенном методе post () .
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален') # и префаером вывели сообщение об удалении
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None): # а в переопределенном методе get_object ( ) отыскали по этому ключу пользователя, подлежащего удалению.
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


def by_rubric(request, pk):
    pass

