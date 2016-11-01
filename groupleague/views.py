from django.shortcuts import render

from .models import Nation


def index(request):
    return render(request, 'groupleague/index.html', {
        'nations': Nation.objects.all(),
    })
