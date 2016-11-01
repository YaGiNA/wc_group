from django.shortcuts import render

from .models import Nation, Game


def addresult_win(Nation):
    Nation.wins += 1
    Nation.points += 3
    print(Nation.points)

def addresult_lose(Nation):
    Nation.loses += 1
    print(Nation.points)


def addresult_draw(Nation):
    Nation.draws += 1
    Nation.points += 1
    print(Nation.points)


def apply_results(Nation, gget, glost):
    Nation.get_goal += gget
    Nation.lost_goal += glost
    Nation.goal_diff = Nation.get_goal - Nation.lost_goal
    if gget > glost:
        addresult_win(Nation)
    elif gget == glost:
        addresult_draw(Nation)
    else:
        addresult_lose(Nation)
    Nation.save()



def index(request):
    games = Game.objects.all()
    for game in games:
        apply_results(game.team, game.team_score, game.opposite_score)


    return render(request, 'groupleague/index.html', {
        'nations': Nation.objects.all(),
    })
