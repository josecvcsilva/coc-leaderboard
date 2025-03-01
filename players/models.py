from django.db import models

class Player(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    town_hall_level = models.IntegerField()
