from django import forms
from .models import *

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = UserAlbumRating
        exclude = ['userOwner']