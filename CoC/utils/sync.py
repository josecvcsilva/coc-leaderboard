from CoC.settings import MAIN_CLAN_TAG
from CoC.utils.coc_api import get_players, get_current_war
from CoC.utils.wars import create_war, create_war_player, create_war_player_attack
from players.models import Player
from CoC.utils.players import create_player, update_player, find_or_create_player_by_tag
from datetime import datetime

from wars.models import War

def players(clan_tag: str = MAIN_CLAN_TAG):
    response_players = get_players(clan_tag)

    if response_players.status_code == 200:
        for player in response_players.json()["items"]:
            if Player.objects.filter(tag=player["tag"]).exists():
                update_player(player["tag"], player["name"], player["townHallLevel"], clan_tag)
                continue
            create_player(player["name"], player["tag"], player["townHallLevel"], clan_tag)

def current_war(clan_tag: str = MAIN_CLAN_TAG):
    response_wars = get_current_war(clan_tag)
    war_data = response_wars.json()

    if response_wars.status_code == 200 and "preparationStartTime" in war_data:
        date_format = "%Y%m%dT%H%M%S.%fZ"
        start_time = datetime.strptime(war_data["preparationStartTime"], date_format)

        # if this war already exist, don't create it again
        if War.objects.filter(start_time=start_time).exists():
            return

        # we only want to save ended wars with no battle modifier
        if war_data["state"] == "warEnded" and war_data["battleModifier"] == "none":
            opponent_clan_tag = war_data["opponent"]["tag"]

            #sync opponents players
            players(opponent_clan_tag)
            curr_war = create_war(opponent_clan_tag, war_data["opponent"]["name"], start_time)

            for attacker in war_data["clan"]["members"]:
                clan_player = find_or_create_player_by_tag(attacker["tag"])
                war_player = create_war_player(clan_player, curr_war, attacker["townhallLevel"])
                if "attacks" in attacker:
                    for attack in attacker["attacks"]:
                        opponent_player = find_or_create_player_by_tag(attack["defenderTag"])
                        create_war_player_attack(war_player, opponent_player.town_hall_level, attack["stars"], attack["destructionPercentage"], attack["defenderTag"],opponent_player.name, attack["order"])