from datetime import datetime

from players.models import Player
from wars.models import War, War_player, War_player_attack


def create_war(opponent_clan_tag: str, clan_name: str, start_time: datetime) -> War:
    new_war = War()
    new_war.opponent_clan_tag = opponent_clan_tag
    new_war.opponent_clan_name = clan_name
    new_war.start_time = start_time
    new_war.save()
    return new_war

def create_war_player(player: Player, war: War, town_hall_level) -> War_player:
    new_war_player = War_player()
    new_war_player.player_id = player.id
    new_war_player.war_id = war.id
    new_war_player.town_hall_level = town_hall_level
    new_war_player.save()
    return new_war_player

def create_war_player_attack(war_player: War_player, defender_town_hall_level, stars, destruction, opponent_tag, opponent_name, order) -> War_player_attack:
    war_player_attack = War_player_attack()
    war_player_attack.war_player_id = war_player.id
    war_player_attack.defender_town_hall_level = defender_town_hall_level
    war_player_attack.stars = stars
    war_player_attack.destruction = destruction
    war_player_attack.opponent_tag = opponent_tag
    war_player_attack.opponent_name = opponent_name
    war_player_attack.order = order
    war_player_attack.save()
    return war_player_attack