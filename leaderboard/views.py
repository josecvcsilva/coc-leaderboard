from datetime import date, datetime

from django.shortcuts import render

from CoC.utils.sync import current_war, players
from leaderboard.dtos.leaderboard import LeaderboardDto
from wars.models import War


def index(request):
    #sync players and current war
    players()
    current_war()

    date_filter = request.GET.get('date')
    date_filter = datetime.strptime(date_filter,'%Y-%m') if date_filter else date.today()
    leaderboard = LeaderboardDto(War.objects.filter(start_time__month__gte=date_filter.month, start_time__year=date_filter.year))
    data = leaderboard.to_dict()
    data['war_dates'] = _get_filter_dates()
    data['last_war'] = War.objects.order_by('-start_time').first()

    return render(request, 'leaderboard.html', data)

# Get distinct dates from Wars and return Month and Year
# Exclude current month from the list
def _get_filter_dates():
    dates = War.objects.all().order_by("-start_time").values("start_time")
    current_month = datetime.today().strftime('%Y-%m')
    war_dates = []
    for war_date in dates:
        formated_war_date = war_date["start_time"].strftime('%Y-%m')
        if formated_war_date not in war_dates and formated_war_date != current_month:
            war_dates.append(formated_war_date)
    return war_dates
