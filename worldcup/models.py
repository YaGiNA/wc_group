from django.db import models


class Nation(models.Model):

    class Meta:
        verbose_name = 'チーム'
        verbose_name_plural = 'チームら'
        ordering = ['-points', '-goal_diff', '-get_goal']
        # priority: points -> goal_diff -> get_goal


    standings = models.IntegerField(default=0)
    nation_name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    percentage = models.FloatField(default=0.000)
    get_goal = models.IntegerField(default=0)
    lost_goal = models.IntegerField(default=0)
    goal_diff = models.IntegerField(default=0)

    def __str__(self):
        return self.nation_name


class Game(models.Model):

    class Meta:
        verbose_name = '試合'
        verbose_name_plural = '試合'

    team = models.ForeignKey(Nation, related_name='team', default="")
    team_score = models.IntegerField(default=0)
    opposite = models.ForeignKey(Nation, related_name='oppo', default="")
    opposite_score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.team) + " vs. " + str(self.opposite)
