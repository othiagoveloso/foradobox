from django.shortcuts import render
import requests
from lisboaiMain.core.models import Categories,Article,Social

# Create your views here.


def index(request,template_name="index.html"): 

    objArticle = Article.objects.all()
    
    return render(request,template_name,{'articles':objArticle})


def post(request,slug):

    objPost = Article.objects.filter(slug=slug)

    return render(request,"post.html",{"post":objPost})



def pageArticle(request,id):

    objArticle = Article.objects.filter(id=id)
        
    return render(request,"portugal.html",{"articles":objArticle})

    
def aboutUs(request,template_name="about.html"):

    return render(request,template_name)


def contact(request,template_name="contato.html"):

    return render(request,template_name)    