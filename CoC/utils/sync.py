from CoC.settings import PORTUGAL_1128_CLAN_TAG
from CoC.utils.coc_api import get_players
from players.models import Player
from CoC.utils.players import create_player, update_player


def players(clan_tag: str = PORTUGAL_1128_CLAN_TAG):
    response_players = get_players(clan_tag)

    print(response_players.json())

    if response_players.status_code == 200:
        for player in response_players.json()["items"]:
            if Player.objects.filter(tag=player["tag"]).exists():
                update_player(player["tag"], player["name"], player["townHallLevel"], clan_tag)
                continue
            create_player(player["name"], player["tag"], player["townHallLevel"], clan_tag)
