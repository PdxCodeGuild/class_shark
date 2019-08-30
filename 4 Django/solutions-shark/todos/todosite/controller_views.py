from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # user is created and saved from form data
            username = form.cleaned_data['username']
            password = form.clean_password2()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('todos:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
