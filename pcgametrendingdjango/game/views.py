from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Review

def games(request):
    return render(request, 'games.html')
