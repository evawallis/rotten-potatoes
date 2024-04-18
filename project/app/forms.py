from django import forms
from .models import *

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = UserAlbumRating
        fields = ['album', 'rating', 'review']
        labels = {'album': 'Album', 'rating': 'Rating (out of 5 stars)', 'review': 'Review'}