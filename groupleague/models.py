from django.db import models


class Nation(models.Model):
    class Meta:
        verbose_name = '参加国'
        verbose_name_plural = '参加国ら'


    nation_name =     models.CharField(max_length=200)
    points =          models.IntegerField(default=0)
    wins =            models.IntegerField(default=0)
    loses =           models.IntegerField(default=0)
    draws =           models.IntegerField(default=0)
    get_goal =        models.IntegerField(default=0)
    lose_goal =       models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)

    def __str__(self):
        return self.nation_name


class Game(models.Model):
    team = models.ForeignKey(Nation, related_name='home_nation_name', default = "")
    team_score = models.IntegerField(default=0)
    opposite = models.ForeignKey(Nation, related_name='away_nation_name', default = "")
    opposite_score = models.IntegerField(default=0)
    # 対戦カード、スコアをタプルで定義する

    def __str__(self):
        return str(self.home) + " vs. " + str(self.away)
