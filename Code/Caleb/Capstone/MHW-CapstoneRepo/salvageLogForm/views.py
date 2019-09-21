from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonalInfoForm

# Create your views here.
def salvageLogForm(request):
    form = PersonalInfoForm()
    return render(request, 'logs/base.html', {'form': form})

    if request.method == "POST":
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()