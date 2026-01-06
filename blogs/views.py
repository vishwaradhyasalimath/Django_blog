from django.shortcuts import redirect, render
from django.http import HttpResponse

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