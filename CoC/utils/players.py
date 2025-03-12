from CoC.utils.coc_api import get_player
from players.models import Player


def create_player (name, tag, town_hall_level, clan_tag) -> Player:
    new_player = Player()
    new_player.name = name
    new_player.tag = tag
    new_player.town_hall_level = town_hall_level
    new_player.clan_tag = clan_tag
    new_player.save()
    return new_player

def update_player (tag, name, town_hall_level, clan_tag) -> Player:
    player = Player.objects.get(tag=tag)
    player.name = name
    player.town_hall_level = town_hall_level
    player.clan_tag = clan_tag
    player.save()
    return player

def find_or_create_player_by_tag(tag: str) -> Player:
    if not Player.objects.filter(tag=tag).exists():
        player = get_player(player_tag=tag).json()
        clan_tag = player["clan"]["tag"] if "clan" in player else ""
        return create_player(player["name"], tag, player["townHallLevel"], clan_tag)
    return Player.objects.filter(tag=tag).first()