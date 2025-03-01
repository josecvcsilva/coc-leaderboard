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