 from django.db import models

class Nation(models.Model):
    nation_name = models.CharField(max_length=200)
    wins =        models.IntegerField(default=0)
    loses =       models.IntegerField(default=0)
    draws =       models.IntegerField(default=0)
    get_points =  models.IntegerField(default=0)
    lose_points = models.IntegerField(default=0)
