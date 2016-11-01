from django.contrib import admin

# Register your models here.
from .models import Nation, Game


admin.site.register(Nation)
admin.site.register(Game)
