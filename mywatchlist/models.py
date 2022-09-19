from pyexpat import model
from django.db import models

# Create your models here.
class WatchlistItem(models.Model):
    watched = models.CharField(max_length=50)
    title = models.CharField(max_length=225)
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()