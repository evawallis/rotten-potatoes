from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

# TODO:

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

# class Person(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     follows = models.ManyToManyField("self")

#     def __str__(self):
#         return self.user.username

# class UserAlbumRating(models.Model):
#     user = models.ForeignKey(Person, on_delete=models.CASCADE)
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)
#     rating = models.FloatField()
#     review = models.TextField()