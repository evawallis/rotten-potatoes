from django.shortcuts import render, redirect
from .models import *
from .forms import *

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
         filteredContent = []

         if searchMethod == 'Album':
            queries = Album.objects.all()
         elif searchMethod == 'Song':
            queries = Song.objects.all()
         elif searchMethod == 'Artist':
            queries = Artist.objects.all()
         else:
            people = Person.objects.all()

         for item in queries:
            if item.name in searchContent:
               filteredContent.append(item)

         for person in people:
            if person.user.first_name in searchContent:
               filteredContent.append(person)
            if person.user.username in searchContent:
               filteredContent.append(person)
         
         context = {'searchedItems': filteredContent}
         return render(request, 'app/search.html', context)   

   context = {'form': form}
   return render(request, 'app/search.html', context)