from django.http import HttpResponse

from CoC.utils import sync


def index(request):
    sync.current_war()
    return HttpResponse("all wars imported")