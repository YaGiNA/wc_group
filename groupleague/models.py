 from django.db import models


class Nation(models.Model):
    class Meta:
        wins_lb = '勝利'
        loses_lb = '敗北'
        draws_lb = '引分'
        get_goal_lb = '得点'
        lose_goal_lb = '失点'
        goal_difference_lb = '得失点差'
        table_name = '順位表'

    nation_name =     models.CharField(max_length=200)
    wins =            models.IntegerField(default=0)
    loses =           models.IntegerField(default=0)
    draws =           models.IntegerField(default=0)
    get_goal =        models.IntegerField(default=0)
    lose_goal =       models.IntegerField(default=0)
    goal_difference = self.get_goal - self.lose_goal


class Game(models.Model):
    class Meta:
        game_card_lb = '試合'
        game_score = '結果'

    game_card = models.ForeignKey(Nation, Nation)
    game_score = (models.IntegerField(default=0), models.IntegerField(default=0))
    # 対戦カード、スコアをタプルで定義する
