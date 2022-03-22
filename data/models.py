from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class ItunesApple(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True )
    genres = models.CharField(max_length=50, null=True, blank=True )
    price = models.PositiveIntegerField()
    artistName = models.CharField(max_length=35, null=True, blank=True)
    artistId = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.artistName}: {self.price}'