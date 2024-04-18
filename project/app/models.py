from django.db import models
from users.models import Person

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=30)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserAlbumRating(models.Model):
    userOwner = models.ForeignKey(Person, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField()