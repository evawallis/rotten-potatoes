from django.db import models
from users.models import Person
from django.core.validators import MinValueValidator, MaxValueValidator

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
    rating = models.DecimalField(decimal_places=1, max_digits=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField()