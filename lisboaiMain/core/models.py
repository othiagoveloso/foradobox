from django.db import models
from django.contrib.auth.models import User


# retorno para status 
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),    
)

class Categories(models.Model):

    name = models.CharField(max_length=100)


    def __unicode__(self): 
        return (self.name)

    def __str__(self):
        return self.name    
    

class Article(models.Model):

    categories = models.ForeignKey('Categories',on_delete=False)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    body = models.TextField(max_length=500,blank=True)
    image = models.URLField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=1, choices=STATUS_CHOICES)
    spotlight = models.BooleanField(default=False)


    def __unicode__(self): 
        return (self.title)

    def __str__(self):
        return self.title 

             


class Social(models.Model):

    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200, blank=True)
    icon = models.CharField(max_length=100)

    def __unicode__(self): 
        return (self.name)
