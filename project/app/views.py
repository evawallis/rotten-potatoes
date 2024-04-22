from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
   for user in User.objects.all():
      try:
         user.person
      except ObjectDoesNotExist:
         person = Person(user=user, favoriteColor="green")
         person.save()
      for follower in user.person.follows.all():
         if follower == user.person:
            user.person.follows.remove(follower)
   return render(request, 'app/index.html')

def profile(request):
   person = request.user.person
   albums = UserAlbumRating.objects.filter(userOwner = person).all()
   context = {'albums': albums}
   return render(request, 'app/profile.html', context)

def add(request):
   if request.method != 'POST':
      form = AddReviewForm()
   else:
      form = AddReviewForm(data=request.POST)
      if form.is_valid():
         message = ""
         instance = form.save(commit=False)
         instance.userOwner = request.user.person
         if instance.rating >= 5.0:
            message = "Rating must be between 0 and 5"
            context = {'form': form, "message": message}
            return render(request, 'app/add.html', context)
         instance.save()
         return redirect('app:profile')
   context = {'form': form}
   return render(request, 'app/add.html', context)

def search(request):
   if request.method != 'POST':
      form = SearchForm()
   else:
      form = SearchForm(data=request.POST)
      if form.is_valid():

         searchContent = form.cleaned_data['searchContent']
         searchMethod = form.cleaned_data['searchMethod']
         queries = []
         people = []

         if searchMethod == 'Album':
            queries = Album.objects.filter(name__icontains=searchContent)
         elif searchMethod == 'Song':
            queries = Song.objects.filter(name__icontains=searchContent)
         elif searchMethod == 'Artist':
            queries = Artist.objects.filter(name__icontains=searchContent)
         else:
            for person in Person.objects.all():
               personName = person.__str__()
               if searchContent in personName:
                  people.append(person)

         context = {'queries': queries, 'people': people}
         return render(request, 'app/search.html', context)   

   context = {'form': form}
   return render(request, 'app/search.html', context)

def user(request, username):
   if request.user.username == username:
      return redirect('app:profile')
   people = Person.objects.all()
   savedPerson = None
   for person in people:
      if person.user.username == username:
         savedPerson = person
   if request.method == 'POST':
      me = request.user.person
      if 'unfollow' in request.POST:
         me.follows.remove(savedPerson)
      elif 'follow' in request.POST:
         me.follows.add(savedPerson)
      me.save()
      return redirect('app:user', username=username)
   albums = UserAlbumRating.objects.filter(userOwner = savedPerson).all()
   context = {'username': username, 'person': savedPerson, 'albums': albums}
   return render(request, 'app/user.html', context)

def album(request, albumid):
   album = Album.objects.all().get(id=albumid)
   reviews = UserAlbumRating.objects.all().filter(album = album)
   context = {'album': album, 'reviews': reviews}
   return render(request, 'app/album.html', context)