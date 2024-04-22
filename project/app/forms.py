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

class SearchForm(forms.Form):
    searchContent = forms.CharField(max_length=50, label="")
    searchMethod = forms.ChoiceField(choices=METHOD_CHOICES, label="Filter by:")