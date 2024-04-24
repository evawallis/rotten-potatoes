from django.contrib import admin
from .models import *

# Custom admin class
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist')
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# Register your models here.
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(UserAlbumRating)