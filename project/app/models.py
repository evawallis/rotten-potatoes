from django.db import models

# Create your models here.

""" TODO:"""
""" add classes user, user following relationship """

class Album(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=30)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class AlbumArtistRelationship(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return("{self.album.name} by {self.artist.name}")