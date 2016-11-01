from django.shortcuts import render

from .models import Nation, Game


def addresult_win(Nation):
    Nation.wins += 1
    points += 3

def addresult_lose(Nation):
    Nation.loses += 1

def addresult_draw(Nation):
    Nation.draws += 1
    points += 1

def apply_results(Nation, gget, glost):
    Nation.get_goal += gget
    Nation.lost_goal += glost
    Nation.goal_diff = Nation.get_goal - Nation.lost_goal
    if gget > glost:
        addresult_win()
    elif gget == glost:
        addresult_draw()
    else:
        addresult_lose()


def index(request):
    return render(request, 'groupleague/index.html', {
        'nations': Nation.objects.all(),
    })
