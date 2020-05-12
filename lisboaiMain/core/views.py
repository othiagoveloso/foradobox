from django.shortcuts import render
import requests
from lisboaiMain.core.models import Categories,Article,Social
from lisboaiMain.core.forms import PostForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request,template_name="index.html"):  
    objArticle = Article.objects.filter(state='p').order_by('-updated')
    
    return render(request,template_name,{'articles':objArticle})


def post(request,slug):
    objPost = Article.objects.filter(slug=slug)

    return render(request,"post.html",{"post":objPost})



def pageArticle(request,nameUrl):
    objArticle = Article.objects.all().filter(categories__nameUrl=nameUrl)
   
    return render(request,"artigos.html",{"articles":objArticle})

    
def aboutUs(request,template_name="about.html"):
    return render(request,template_name)


def contact(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PostForm()
        messages.success(request, 'Sua mensagem foi enviada :)')
    return render(request, 'contato.html', {'form': form})




