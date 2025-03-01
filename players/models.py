from django.db import models

class Player(models.Model):

    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    town_hall_level = models.IntegerField()
    clan_tag = models.CharField(max_length=20, null=True)
