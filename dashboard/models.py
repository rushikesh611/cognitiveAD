from django.db import models
# Create your models here.
class Game(models.Model):
    gametype = models.CharField(max_length=100)
    titlegame1 = models.CharField(max_length=100)
    titlegame2 = models.CharField(max_length=100)
    descriptiongame1 = models.TextField()
    descriptiongame2 = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    game1url = models.CharField(max_length=100)
    game2url = models.CharField(max_length=100)

    def __str__(self):
        return self.gametype
    