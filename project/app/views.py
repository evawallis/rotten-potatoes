from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
   return render(request, 'app/index.html')

def profile(request):
   currentUser = request.user
   if currentUser.person:
      person = currentUser.person
   else:
      person = Person.objects.create(user=currentUser)

   albums = UserAlbumRating.objects.filter(userOwner = person).all()
   context = {'albums': albums}
   return render(request, 'app/profile.html', context)