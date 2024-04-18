from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import PersonForm
from .models import *

# Create your views here.
def register(request):
    if request.method != 'POST': # GET: No data; create a blank form
        form = UserCreationForm()
        personForm = PersonForm()
    else: # POST: Data submitted; process data: validate and store
        form = UserCreationForm(data=request.POST)
        personForm = PersonForm(data=request.POST)
        if form.is_valid() and personForm.is_valid():
            savedUser = form.save()
            person = personForm.save(commit = False)
            person.user = savedUser
            person.save()
            return redirect('app:home')
    context = {'form': form, 'person_form': personForm} # executed if the form was not valid
    return render(request, 'registration/register.html', context)