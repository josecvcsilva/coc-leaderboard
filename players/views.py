from django.http import HttpResponse

from CoC.utils.coc_api import get_players


def index(request):

    return HttpResponse(get_players())