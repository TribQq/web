from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# from .models import AdvUser
# from .forms import ChangeUserInfoForm
from .models import *
from .forms import *


def index1(request) -> render:
    return render(request, 'main/index.html')


def other_page(request, page: str) -> HttpResponse:
    try:
        template = get_template('main/'+page+'.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class BBLoginView(LoginView):
    template_name: str = 'main/user/login.html'


class BBLogoutView(LoginView):
    template_name: str = 'main/user/logout.html'


@login_required
def profile(request):
    return render(request, 'main/user/profile.html')


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    form_class = ChangeUserInfoForm
    template_name = 'main/user/change_user_info.html'
    success_url = reverse_lazy('profile')
    success_message = 'User data changed'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class NoteView(SuccessMessageMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'main/test_template.html'
    success_url = reverse_lazy('top10')
    success_message = 'note updated'
    def get_object(self, queryset=None):
        return get_object_or_404(Note, id=6) # захардкоженная нота котрую берём и upd по запросу

