from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # user is created and saved from form data
            username = form.cleaned_data['username']
            password = form.clean_password2()
            user = authenticate(username=username, password=password)
            if user:
                group = Group.objects.get(name='Commenter')
                user.groups.add(group)
                login(request, user)
            return redirect('vue:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'