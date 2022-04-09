
from django.shortcuts import render, redirect
from django.http import Http404,HttpResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView
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

from .models import AdvUser, SubRubric, Bb, Comment
from .forms import ChangeUserInfoForm, RegisterUserForm, SearchForm, AIFormSet, BbForm, UserCommentForm, GuestCommentForm
from .utilities import signer


def index(request):
    """ render main page bbs(ads) limit = first 10"""
    bbs = Bb.objects.filter(is_active=True)[:10]
    context = {'bbs': bbs}
    return render(request, 'main/index.html', context)


def other_page(request, page):
    """ get template or 404"""
    try:
        template = get_template('main/' + page +'.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class BBLoginView(LoginView):
    """ view for login , sumbit => redirect to /accounts/profile"""
    template_name = 'main/login.html'


@login_required
def profile(request):
    """ get only the current user of the bbs(ads)"""
    bbs = Bb.objects.filter(author=request.user.pk)
    context = {'bbs': bbs}
    return render(request, 'main/profile.html', context)


class BBLogoutView(LoginRequiredMixin, LogoutView): # LoginRequiredMixin - чек регистрации + чек входа
    template_name = 'main/logout.html'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ change the curent user info data and """
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('bulletin_board:profile')
    success_message = 'Данные изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    """ view for change user pass """
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('bulletin_board:profile')
    success_message = 'Пароль изменён'


class BBPasswordResetView(PasswordResetView):
    """ view for drop user pass with email  """
    template_name = 'main/password_reset.html' # взять с кнопки реги отправку письма на почту
    subject_template_name = 'email/reset_letter_subject.txt'
    email_template_name = 'email/reset_letter_body.txt'
    success_url = reverse_lazy('bulletin_board:password_reset_done')


class BBPasswordResetDoneView(PasswordResetDoneView):
    """ reset pass"""
    template_name = 'main/password_reset_done.html'


class BBPasswordResetConfirmView(PasswordResetConfirmView):
    """ confirm reset pass"""
    template_name = 'main/password_confirm.html'
    success_url = reverse_lazy('bulletin_board:password_reset_complete')


class BBPasswordResetCompleteView(PasswordResetCompleteView):
    """ complete reset pass """
    template_name = 'main/password_complete.html'


class RegisterUserView(CreateView):
    """ view for register user"""
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('bulletin_board:register_done')


class RegisterDoneView(TemplateView):
    """ user register done"""
    template_name = 'main/register_done.html'


def user_activate(request, sign):
    """ user acc activation"""
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html') # перенаправление в случае неудачи
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user_is_activated.html' # в случае уже активиров
    else:
        template = 'main/activation_done.html' # актив завершен
        user.is_active = True
        user.is_activated = True
        user.save() # активируем
    return render(request, template)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    """ delete user acc"""
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('bulletin_board:index')

    def setup(self,request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


def by_rubric(request, pk):
    """ only current rubric bbs(ads) + pagination"""
    rubric = get_object_or_404(SubRubric, pk=pk)
    bbs = Bb.objects.filter(is_active=True, rubric=pk)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title_icontains=keyword) | Q(content__icontains=keyword)
        bbs = bbs.filter(q)
    else:
        keyword = ''
    form = SearchForm(initial={'keyword': keyword})
    paginator = Paginator(bbs, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    contex = {'rubric': rubric, 'page': page, 'bbs': page.object_list, 'form': form}
    return render(request, 'main/by_rubric.html', contex)


def detail(request, rubric_pk, pk):
    """ detail about bb(ad)"""
    bb = get_object_or_404(Bb, pk=pk)
    ais = bb.additionalimage_set.all() # пикчи
    comments = Comment.objects.filter(bb=pk, is_active=True)
    initial = {'bb': bb.pk}
    if request.user.is_authenticated:
        initial['author'] = request.user.username
        form_class = UserCommentForm
    else:
        form_class = GuestCommentForm
    form = form_class(initial=initial)
    if request.method == 'POST':
        c_form = form_class(request.POST)
        if c_form.is_valid():
            c_form.save()
            messages.add_message(request,messages.SUCCESS, 'Комментарий добавлен')
        else:
            form = c_form
            messages.add_message(request,messages.WARNING, 'Комментарий не был добавлен')
    context = {'bb': bb, 'ais': ais, 'comments': comments, 'form': form}
    return render(request, 'main/detail.html', context)


@login_required
def profile_bb_detail(request, pk):
    """ profile bb detail """
    bb = get_object_or_404(Bb, pk=pk)
    ais = bb.additionalimage_set.all()
    # comments = Comment.objects.filter(bb=pk, is_active=True)
    context = {'bb': bb, 'ais': ais}
    return render(request, 'main/profile_bb_detail.html', context)


@login_required
def profile_bb_add(request): # only adm now
    """ add bb from profile page """
    if request.method == 'POST':
        form = BbForm(request.POST, request.FILES)
        if form.is_valid():
            bb = form.save()
            formset = AIFormSet(request.POST, request.FILES, instance=bb)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Обьявление добавлено')
                return redirect('bulletin_board:profile')
    else:
        form = BbForm(initial={'author': request.user.pk})
        formset = AIFormSet()
    context = {'form': form, 'formset': formset}
    return render(request, 'main/profile_bb_add.html', context)


@login_required
def profile_bb_change(request,pk):
    """ change bb from profile page"""
    bb = get_object_or_404(Bb, pk=pk)
    if request.method == 'POST':
        form = BbForm(request.POST, request.FILES, instance=bb)
        if form.is_valid():
            bb = form.save()
            formset = AIFormSet(request.POST, request.FILES, instance=bb)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Обьявление исправлено')
                return redirect('bulletin_board:profile')
    else:
        form = BbForm(instance=bb)
        formset = AIFormSet(instance=bb)
    context = {'form': form, 'formset': formset}
    return render(request, 'main/profile_bb_change.html', context)


@login_required
def profile_bb_delete(request, pk):
    """ delete bb from profile """
    bb = get_object_or_404(Bb, pk=pk)
    if request.method == 'POST':
        bb.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Объявление удалено')
        return redirect('bulletin_board:profile')
    else:
        context = {'bb': bb}
        return render(request, 'main/profile_bb_delete.html', context)


