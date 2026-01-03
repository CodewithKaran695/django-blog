from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from blogs.models import Blog, Category

# Create your views here.
def posts_by_category(request,category_id):
    # fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Publish',category=category_id)
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the use to home page
    #     return redirect('home')

    category = get_object_or_404(Category,pk=category_id)
    context = {
        'posts':posts,
        'category':category
    }
    return render(request,'post_by_category.html',context)