from django.contrib import admin
from players.models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["tag","name", "clan_tag", "town_hall_level"]
    ordering = ["tag", "name", "clan_tag", "town_hall_level"]
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
