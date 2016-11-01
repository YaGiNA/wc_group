from django.contrib import admin

# Register your models here.
from .models import Nation, Game


class NationAdmin(admin.ModelAdmin):
    list_display = ('nation_name', 'points',
    'games', 'wins', 'loses', 'draws', 'percentage',
    'get_goal', 'lost_goal', 'goal_diff')


admin.site.register(Nation, NationAdmin)
admin.site.register(Game)
