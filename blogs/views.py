from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.db.models import Q

from .models import Blog, Category
# Create your views here.
def posts_by_category(request,category_id):
    '''Fetch the posts that belong to the category with the id categorty_id'''
    posts = Blog.objects.filter(status ='Published',category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        #redirect the user to home page
        return redirect('home')
    '''can also use 404 error page : category = get_object_or_404(category,pk = category_id)'''
    context = {
        'posts':posts,
        'category':category,
    }
    return render(request,'post_by_category.html',context)

''' this is for slug to be used in the url'''
def blogs(request,slug):
    single_blog = get_object_or_404(Blog, slug=slug, status = 'Published')
    context = {
        'single_blog':single_blog,
    }
    return render(request,'blogs.html',context)


def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains=keyword)| Q(blog_body__icontains=keyword),status='Published')
    context = {
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request,'search.html',context)