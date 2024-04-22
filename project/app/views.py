from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User

# Create your views here.
def home(request):
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
   people = Person.objects.all()
   for person in people:
      if person.user.username == username:
         savedPerson = person
   albums = UserAlbumRating.objects.filter(userOwner = savedPerson).all()
   context = {'person': savedPerson, 'albums': albums}
   return render(request, 'app/user.html', context)