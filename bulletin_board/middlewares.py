

from .models import SubRubric


def bboard_context_processor(request):
    """ pagination
    'keyword'- GET parameter, which will be needed to generate Internet addresses in paginator hyperlinks;
    'all'- with the 'keyword' and 'page' GET parameters that we will add to the Internet URLs of hyperlinks pointing to add detail pages.
    """
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    context['keyword'] = ''
    context['all'] = ''
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
