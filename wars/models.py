from django.db import models

from players.models import Player


class War(models.Model):
    id = models.AutoField(primary_key=True)
    opponent_clan_tag = models.CharField(max_length=20)
    opponent_clan_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()


class War_player(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    war = models.ForeignKey(War, on_delete=models.CASCADE)
    town_hall_level = models.IntegerField()

class War_player_attack(models.Model):
    id = models.AutoField(primary_key=True)
    war_player = models.ForeignKey(War_player, on_delete=models.CASCADE)
    defender_town_hall_level = models.IntegerField()
    stars = models.IntegerField()
    destruction = models.IntegerField()
    opponent_tag = models.CharField(max_length=20)
    opponent_name = models.CharField(max_length=100)
    order = models.IntegerField()
