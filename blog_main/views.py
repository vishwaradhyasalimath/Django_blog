
from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Blog, Category
from utility.models import About


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