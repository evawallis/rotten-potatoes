from django import forms
from .models import *

METHOD_CHOICES =[
    ("Album", "Album"), 
    ("Artist", "Artist"), 
    ("Song", "Song"), 
    ("User", "User")
    ]

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = UserAlbumRating
        exclude = ['userOwner']

    def clean(self):
        cleaned_data = super().clean()
        album = cleaned_data.get('album')
        user = cleaned_data.get('userOwner')
        rating = cleaned_data.get('rating')

        # Check if the user has already rated the album
        if album and user:
            existing_rating = UserAlbumRating.objects.filter(album=album, userOwner=user).first()
            if existing_rating:
                # Update the existing rating with the new value
                existing_rating.rating = rating
                existing_rating.save()
                # Delete the previous rating
                existing_rating.delete()
                # Do not raise validation error as the rating is being updated

        return cleaned_data

class SearchForm(forms.Form):
    searchContent = forms.CharField(max_length=50, label="")
    searchMethod = forms.ChoiceField(choices=METHOD_CHOICES, label="Filter by:")