
from multiprocessing import AuthenticationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blog_main.forms import RegistrationForm
from blogs.models import Blog, Category
from utility.models import About
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    ''' Display cateogries,featured post on the Home page'''
    # categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True,status = 'Published')
    posts = Blog.objects.filter(is_featured= False,status = 'Published')
    #fetch about us
    try:
        about = About.objects.get()
    except:
        pass
    context = {
        # 'categories':categories,
        'featured_post':featured_post,
        'posts':posts,
        'about':about,
    }

    return render(request, 'home.html',context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request, 'register.html',context)


def login(request):
    #default authentication form 
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user =auth.aauthenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('home')