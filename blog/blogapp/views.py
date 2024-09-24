from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Category


# Create your views here.

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category_id')
        if request.user.is_authenticated:
            category = Category.objects.get(id=int(category_id))
            new_post = Post(title = title, content = content, category = category, author = request.user)
            new_post.save()
        else:
            redirect('login')

    categories = Category.objects.all()
    return render(request, 'home.html', {'categories' : categories})


def myblogs(request):
    
    user_posts = Post.objects.filter(author = request.user)
    return render(request, 'myblogs.html', {'blogs':user_posts})

def delete(request):
    blog =''
    if request.method == 'POST':
        title = request.POST.get('getblog')
        blog = Post.objects.filter(title = title, author = request.user).first()

        if blog:
            blog.delete()
        else:
            return HttpResponse("No such blog found :(")
        
    return render(request, 'delete.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form' : form})
