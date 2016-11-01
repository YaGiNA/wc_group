from django.shortcuts import render

from .models import Nation, Game


def initial():
    nations = Nation.objects.all()
    for nation in nations:
        nation.points = 0
        nation.games = 0
        nation.wins = 0
        nation.loses = 0
        nation.draws = 0
        nation.percentage = 0
        nation.get_goal = 0
        nation.lost_goal = 0
        nation.goal_diff = 0
        nation.save()

    games = Game.objects.all()
    for game in games:
        swap_result(game.team, game.team_score,
                    game.opposite, game.opposite_score)


def addresult_win(Nation):
    Nation.wins += 1
    Nation.points += 3  # win => add 3 points


def addresult_lose(Nation):
    Nation.loses += 1   # lose => add 0 point


def addresult_draw(Nation):
    Nation.draws += 1
    Nation.points += 1  # draw => add 1 point


def apply_result(Nation, gget, glost):  # Apply to team stats from a result
    Nation.get_goal += gget     # ADD gain
    Nation.lost_goal += glost   # ADD lost
    Nation.goal_diff = Nation.get_goal - Nation.lost_goal
    if gget > glost:
        addresult_win(Nation)
    elif gget == glost:
        addresult_draw(Nation)
    else:
        addresult_lose(Nation)
    Nation.games += 1
    Nation.percentage = round(
        Nation.wins / Nation.games, 3)    # Explode in *.***
    Nation.save()   # Apply complete


def swap_result(team, team_score, oppo, oppo_score):    # Apply to 2 team from 1 game
    apply_result(team, team_score, oppo_score)
    apply_result(oppo, oppo_score, team_score)


def index(request):
    initial()
    return render(request, 'groupleague/index.html', {
        'nations': Nation.objects.all(),
    })
