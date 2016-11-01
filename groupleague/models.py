from django.db import models


class Nation(models.Model):
    nation_name =     models.CharField(max_length=200)
    wins =            models.IntegerField(default=0)
    loses =           models.IntegerField(default=0)
    draws =           models.IntegerField(default=0)
    get_goal =        models.IntegerField(default=0)
    lose_goal =       models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)


class Game(models.Model):
    game_card = models.ForeignKey(Nation, Nation)
    game_score = (models.IntegerField(default=0), models.IntegerField(default=0))
    # 対戦カード、スコアをタプルで定義する
