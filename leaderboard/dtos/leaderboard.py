from django.db.models import QuerySet
from wars.models import War


def _calculate_bonus_stars(stars: int, town_hall_level: int, opponent_town_hall_level) -> int:
    if town_hall_level > opponent_town_hall_level or stars == 1:
        return 0

    return stars - 1


class LeaderboardDto:
    def __init__(self, war_list: QuerySet[War]):
        self.wars = war_list

    def to_dict(self):
        players_data = []
        for war in self.wars:
            for war_player in war.war_player_set.all():
                player = war_player.player
                player_data = next((p for p in players_data if p['tag'] == player.tag), None)
                if not player_data:
                    player_data = {
                        "tag": player.tag,
                        "name": player.name,
                        "town_hall_level": war_player.town_hall_level,
                        "stars": 0,
                        "total_destruction": 0,
                        "total_bonus_stars": 0,
                        "total_stars" : 0,
                        "attacks": [],
                    }
                    players_data.append(player_data)
                for attack in war_player.war_player_attack_set.all():
                    bonus_stars = _calculate_bonus_stars(
                        attack.stars, war_player.town_hall_level, attack.defender_town_hall_level
                    )
                    player_data["stars"] += attack.stars
                    player_data["total_destruction"] += attack.destruction
                    player_data["total_bonus_stars"] += bonus_stars
                    player_data["total_stars"] += (attack.stars + bonus_stars)
                    player_data["attacks"].append({
                        "stars": attack.stars,
                        "destruction": attack.destruction,
                        "bonus_stars": bonus_stars,
                        "defender_name": attack.opponent_name,
                        "defender_town_hall_level": attack.defender_town_hall_level,
                    })
        players_data = sorted(players_data, key=lambda x: (x['total_stars'], x['total_destruction']), reverse=True)
        return {"players": players_data, "max_attacks": len(self.wars) * 2}
