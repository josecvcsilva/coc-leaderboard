from django.http import HttpResponse

from CoC.utils import sync


def index(request):
    sync.players()
    return HttpResponse("all players imported")