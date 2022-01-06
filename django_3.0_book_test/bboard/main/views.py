#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
from django.shortcuts import render, redirect
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
from django.core.paginator import Paginator
from django.db.models import Q

from .models import AdvUser,SubRubric, Bb
from .forms import ChangeUserInfoForm, RegisterUserForm, SearchForm, AIFormSet, BbForm
from .utilities import signer

def index(request):
    bbs = Bb.objects.filter(is_active=True)[:10] # фрагмент, выбирающий из базы последние 1О объявлений:
    context = {'bbs': bbs}
    return render(request, 'main/index.html', context)


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
    bbs = Bb.objects.filter(author=request.user.pk)
    context = {'bbs': bbs}
    return render(request, 'main/profile.html', context)


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
        username = signer.unsign(sign) # Подписанный идентификатор пользователя, передаваемый в составе интернетадреса, получаем с параметром sign. Далее извлекаем из него имя пользователя,
    except BadSignature:
        return render(request, 'main/bad_signature.html') # перенаправление в случае неудачи
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user_is_activated.html' # в случае уже активиров
    else:
        template = 'main/activation_done.html' # актив завершен
        user.is_active = True # делаем его активным, присвоив значения тrue
        user.is_activated = True  # делаем его активным, присвоив значения тrue
        user.save()
    return render(request, template)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')

    def setup(self,request, *args, **kwargs):
        self.user_id = request.user.pk # тоже что и в ChangeUserInfoView: взяли ключ юзера
        return super().setup(request, *args, **kwargs) # В переопределенном методе setup () сохранили ключ текущего пользователя

    def post(self,request, *args, **kwargs): # Перед удалением текущего пользователя необходимо выполнить выход, что мы и сделали в переопределенном методе post () .
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален') # и префаером вывели сообщение об удалении
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None): # а в переопределенном методе get_object ( ) отыскали по этому ключу пользователя, подлежащего удалению.
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


def by_rubric(request, pk): # 639 стр
    rubric = get_object_or_404(SubRubric, pk=pk) # Извлекаем выбранную посетителем рубрику  нам понадобится вывести на странице ее название.
    bbs = Bb.objects.filter(is_active=True, rubric=pk) # Затем выбираем объявления, относящиеся к этой рубрике и помеченные для вывода
    if 'keyword' in request.GET: # о выполняем фильтрацию уже отобранных объявлений по введенному посетителем искомому слову, взятому из GЕТ-параметра keyword
        keyword = request.GET['keyword'] # Ради простоты получаем искомое слово непосредственно из GЕТ-параметра
        q = Q(title_icontains=keyword) | Q(content__icontains=keyword) # формируем на основе полученного слова условие фильтрации, применив объект Q,
        bbs = bbs.filter(q) # выполняем фильтрацию объявлений
    else:
        keyword = ''
    form = SearchForm(initial={'keyword': keyword}) # создаем экземпляр формы SearchForm, чтобы вывести ее на экран
    # Конструктору ее класса в параметре intial передаем полученное ранее искомое слово, чтобы оно присутствовало в выведенной на экран форме.
    paginator = Paginator(bbs, 2) # пагинатор, указав у него количество записей в части равным 2
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    contex = {'rubric': rubric, 'page': page, 'bbs': page.object_list, 'form': form}
    return render(request, 'main/by_rubric.html', contex) # , выводим страницу со списком объявлений


def detail(request, rubric_pk, pk):
    bb = get_object_or_404(Bb, pk=pk) # обьявлений
    ais = bb.additionalimage_set.all() # пикчи
    context = {'bb': bb, 'ais': ais}
    return render(request, 'main/detail.html', context)

@login_required
def profile_bb_detail(request, pk):
    bb = get_object_or_404(Bb, pk=pk) # обьявлений
    ais = bb.additionalimage_set.all() # пикчи
    # comments = Comment.objects.filter(bb=pk, is_active=True)
    context = {'bb': bb, 'ais': ais}
    return render(request, 'main/profile_bb_detail.html', context)


@login_required
def profile_bb_add(request):
    # Важные моменты :
    # 1-при создании формы перед выводом страницы сохранения мы заносим в поле author формы ключ текущего пользователя, который станет автором объявления
    # 2- , во время сохранения введенного объявления, при создании объектов
    # формы и набора форм, мы должны передать конструкторам их классов вторым позиционным параметром словарь со всеми полученными файлами (он хранится
    # в атрибуте FILES объекта запроса). Если мы не сделаем этого, то отправленные пользователем иллюстрации окажутся потерянными.
    # 3- при сохранении мы сначала выполняем валидацию и сохранение формы
    # самого объявления. Метод save () в качестве результата возвращает сохраненную запись, и эту запись мы должны передать через параметр instance конструктору
    # класса набора форм. Это нужно для того, чтобы все дополнительные иллюстрации после сохранения оказались связанными с объявлением
    if request.method == 'POST':
        form = BbForm(request.POST, request.FILLES)
        if form.is_valid():
            bb = form.save()
            formset = AIFormSet(request.POST, request.FILES, instance=bb)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Обьявление добавлено')
                return redirect('main:profile')
    else:
        form = BbForm(initial={'author': request.user.pk})
        formset = AIFormSet()
    context = {'form': form, 'formset': formset}
    return render(request, 'main/profile_bb_add.html', context)
# Обязательно укажем у(в хтмл~е) формы метод кодирования данных mult ipart/ form-data. Если этого не сделать, то занесенные в форму файлы не будут отправлены. А набор форм выведем с помощью тега шаблонизатора boots trap _ formset.


@login_required
def profile_bb_change(request,pk):
    bb = get_object_or_404(Bb,pk=pk)
    if request.method == 'POST':
        form = BbForm(request.POST, request.FILLES)
        if form.is_valid():
            bb = form.save()
            formset = AIFormSet(request.POST, request.FILES, instance=bb)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Обьявление исправлено')
                return redirect('main:profile')
    else:
        form = BbForm(instance=bb)
        formset = AIFormSet(instance=bb)
    context = {'form': form, 'formset': formset}
    return render(request, 'main/profile_bb_change.html', context)

@login_required
def profile_bb_delete(request, pk):

    bb = get_object_or_404(Bb, pk=pk)
    if request.method == 'POST':
        bb.delete()
        messages.add_message(request, messages.SUCCESS, 'Обьявление удалено')
        return redirect('main:profile')
    else:
        context = { 'bb': bb}
        return render(request, 'main/profile_bb_delete.html', context)