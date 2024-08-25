from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    year = models.CharField(max_length=10, default='Unknown')
    genre = models.CharField(max_length=250, default='gen')
    poster = models.CharField(max_length=2083)
    imdbrating = models.CharField(max_length=10, blank=True)
    rated = models.CharField(max_length=10, blank=True) 
    searchCount = models.IntegerField(default=0)

    def __str__(self):
        return self.title
