
from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Blog, Category


def home(request):
    ''' Display cateogries,featured post on the Home page'''
    # categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True,status = 'Published')
    posts = Blog.objects.filter(is_featured= False,status = 'Published')
    print(posts)
    context = {
        # 'categories':categories,
        'featured_post':featured_post,
        'posts':posts,
    }

    return render(request, 'home.html',context)