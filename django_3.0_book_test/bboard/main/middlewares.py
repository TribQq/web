# обработчик контекста, в котором и будет формироваться список подрубрик. 631

from .models import SubRubric


def bboard_context_processor(request):
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    context['keyword'] = '' # keyword - с GЕТ-параметром keyword, который понадобится для генерирования интернет-адресов в гиперссылках пагинатора;
    context['all'] = '' # all -с GЕТ-параметрами keyword и page, которые мы добавим к интернетадресам гиперссьшок, указывающих на страницы сведений об объявлениях.
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            context['keyword'] = '?keyword=' + keyword
            context['all'] = context['keyword']
    if 'page' in request.GET:
        page = request.GET['page']
        if page != '1':
            if context['all']:
                context['all'] += '&page=' + page
            else:
                context['all'] = '?page=' + page
    return context
