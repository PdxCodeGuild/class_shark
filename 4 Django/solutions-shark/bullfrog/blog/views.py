from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from .models import *
from .forms import PostForm

def is_poster(user):
    # user is poster
    poster = Group.objects.get(name='Poster')
    return poster in user.groups.all()

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@user_passes_test(is_poster)
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@user_passes_test(is_poster)
def post_edit(request, pk):
    existing_post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=existing_post)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=existing_post)
    return render(request, 'blog/post_edit.html', {'form': form})

