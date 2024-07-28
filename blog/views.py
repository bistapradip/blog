from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post, Category
import logging
# Create your views here.
def home(request):
    #load all the post from db(10)
    posts =Post.objects.all()[:10]
    categorys = Category.objects.all()
    data = {
        'posts':posts,
        'categorys': categorys
    }
    return render(request, "home.html", data)

def post(request, url): #Yahako url ma user ley click garney value pass Huncha (url.py ma vako url ko value ho)
    post = Post.objects.get(url=url)
    categorys = Post.objects.all()
    print(post)
    print("Test")
    return render(request, 'posts.html', {'post':post, 'categorys':categorys})


def category(request, url):
    category = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=category) # It applies a filter to this query to return only the posts that are related to a specific category.
    return render(request, "category.html",{'category':category, 'posts':posts})

def about(request):
    return render(request,"about.html")
             