from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Review

def game_show(request):
    game = Game.objects.order_by('popularity')
    return render(request, 'game/game_show.html', {'game': game})
