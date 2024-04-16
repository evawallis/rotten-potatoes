from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
   return render(request, 'app/index.html')

def profile(request):
   albums = Album.objects.filter(userOwner = request.user).all
   context = {'albums': albums}
   return render(request, 'app/profile.html', context)