from django.shortcuts import render

# Create your views here.

from .models import Blog


def home(request):
    return render(request, 'app/home.html')


def blog(request):
    list_blog = Blog.objects.all()
    context={
        "list_blog":list_blog
    }
    
    return render(request,"app/blog.html",context)

def detail(request,titre:str):
    
    try:
        blogdetail = Blog.objects.get(titre=titre)
    except Blog.DoesNotExist:
        raise ("le post n'existe pas")
        
    return render(request,"app/detail.html",{"blogdetail":blogdetail})