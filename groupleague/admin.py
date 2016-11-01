from django.contrib import admin

# Register your models here.
from .models import Nation, Game

'''
class GamesInline(admin.StackedInline):
    model = Game
    extra = len(Nation.objects.all()) - 1
    fk_name = 'team'


#class NationAdmin(admin.ModelAdmin):
    inlines = [GamesInline]


admin.site.register(Nation, NationAdmin)
'''
admin.site.register(Nation)
admin.site.register(Game)
