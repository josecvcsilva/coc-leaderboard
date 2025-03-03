from datetime import date, datetime

from django.shortcuts import render

from leaderboard.dtos.leaderboard import LeaderboardDto
from wars.models import War


def index(request):
    date_filter = request.GET.get('date')
    date_filter = datetime.strptime(date_filter,'%Y%M') if date_filter else date.today()

    leaderboard = LeaderboardDto(War.objects.filter(start_time__month__gte=date_filter.month))
    data = leaderboard.to_dict()
    return render(request, 'leaderboard.html', data)

