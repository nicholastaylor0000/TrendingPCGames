from django.db import models

class Game(models.Model):
    name = models.TextField()
    description = models.TextField()
    genre = models.TextField()
    popularity = models.IntegerField()

class Review(models.Model):
    gameName = models.TextField()
    username = models.TextField()
    review = models.TextField()
