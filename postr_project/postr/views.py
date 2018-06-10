from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
# show all posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'postr/post_list.html', {'posts': posts})

# show one post
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'postr/post_detail.html', {'post': post})

# sign up view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'postr/signup.html', {'form': form})

# login required create a post
@login_required
def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user.profile
            post = post_form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        post_form = PostForm()
    return render(request,  'postr/post_form.html', {'form': form})

# login required to create a Comment
@login_required
def comment_create(request, pk):
    post_id = pk
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user.profile
            comment = comment_form.save()
            return redirect('post_detail', pk=post_id)
