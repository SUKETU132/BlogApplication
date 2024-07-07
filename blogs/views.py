from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog_app
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from django.contrib.auth.models import AnonymousUser

# for redirecting the login page
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username doesn't exist")
            return redirect('/blog/login/')
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('/blog/login/')
        else:
            login(request, user)
            return redirect('/')
    
    return render(request, "blog/login.html")

# for redirecting the register page
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        
        if password == confirm_password:
            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already taken.")
            else:
                # Create the user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('/blog/login/')  # Redirect to login page after successful registration
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'blog/register.html')

#  for logout
def logout_page(request):
    logout(request)
    return redirect('/blog/login/')

# for add the post
def add_post(request):
    
    if isinstance(request.user, AnonymousUser):
        return render(request, 'blog/blogs/PostCard.html', {'message': 'You need to login to add post.'})
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.user = request.user
            blog_post.save()
            return redirect('/blog/')
    else:
        form = BlogForm()
    return render(request, 'blog/blogs/add_post.html', {'form': form})

#  for delete post
@login_required
def delete_post(request, id):
    post = get_object_or_404(Blog_app, id=id)
    if request.user != post.user:
        return HttpResponseForbidden("You are not authorized to delete this post.")
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'blog/blogs/delete_post.html', {'post': post})

@login_required
def edit_post(request, id):
    post = get_object_or_404(Blog_app, id=id)
    if request.user != post.user:
        return HttpResponseForbidden("You are not authorized to edit this post.")
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog/blogs/edit_post.html', {'form': form})

# for fetching the data from backend
def fetch_data(request):
    if isinstance(request.user, AnonymousUser):
        return render(request, 'blog/blogs/PostCard.html', {'message': 'You need to login first to see all post.'})
    
    posts = Blog_app.objects.all()
    return render(request, 'blog/blogs/PostCard.html', {'posts': posts}) 

def post_detail(request, id):
    post = get_object_or_404(Blog_app, id=id)
    return render(request, 'blog/blogs/post_detail.html', {'post': post})

def view_user_post(request):
    if isinstance(request.user, AnonymousUser):
        return render(request, 'blog/blogs/PostCard.html', {'message': 'You need to login to view your posts.'})
    
    current_user = request.user
    user_posts = Blog_app.objects.filter(user=current_user)
    return render(request, 'blog/blogs/PostCard.html', {'posts': user_posts})

