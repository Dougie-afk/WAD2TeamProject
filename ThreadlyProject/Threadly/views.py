from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Thread, Post, Comments, User
from .forms import UserForm, PostForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
import cloudinary.uploader

def index(request):
    categories = Thread.objects.order_by('-threadID')[:5]  
    return render(request, 'Threadly/index.html', {'categories': categories})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('Threadly:index')
    else:
        form = UserForm()
    return render(request, 'Threadly/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('Threadly:personalized_feed')
        else:
            return HttpResponse("Invalid login details")
    return render(request, 'Threadly/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('Threadly:index')


def trending(request):
    trending_posts = Post.objects.order_by('-likes')[:10]
    return render(request, 'Threadly/trending.html', {'posts': trending_posts})

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query) if query else []
    return render(request, 'Threadly/search_results.html', {'results': results})


@login_required
def account(request):
    user = request.user
    return render(request, 'Threadly/account.html', {'user': user})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.UserID = request.user
            if request.FILES.get('image'):
                post.photoContent = upload_image(request.FILES['image'])
            post.save()
            return redirect('Threadly:show_post', post_id=post.postID)
    else:
        form = PostForm()
    return render(request, 'Threadly/create_post.html', {'form': form})

# Show posts under categories
def show_category(request, slug):
    category = get_object_or_404(Thread, slug=slug)
    posts = Post.objects.filter(threadID=category).order_by('-postID')
    return render(request, 'Threadly/categories.html', {'category': category, 'posts': posts})

# Displays individual posts and comments
def show_post(request, post_id):
    post = get_object_or_404(Post, postID=post_id)
    comments = Comments.objects.filter(postID=post)
    return render(request, 'Threadly/post.html', {'post': post, 'comments': comments})
# Add a comment (login required)
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, postID=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.userID = request.user
            comment.postID = post
            comment.save()
            return redirect('Threadly:show_post', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'Threadly/add_comment.html', {'form': form, 'post': post})
# Follow Topics (login required)
@login_required
def follow_thread(request, thread_id):
    thread = get_object_or_404(Thread, threadID=thread_id)
    request.user.follows.add(thread)
    return redirect('Threadly:show_category', slug=thread.slug)

# Image upload helper
def upload_image(file):
    result = cloudinary.uploader.upload(file)
    return result['secure_url']