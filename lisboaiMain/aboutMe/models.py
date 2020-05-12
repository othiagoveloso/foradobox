from django.db import models

# Create your models here.

TYPE_EXPERIENCE = (
    ('c', 'Company'),
    ('p', 'Project'),    
)


TYPE_EDUCATION = (
    ('w', 'Workshop'),
    ('c', 'Course'),
    ('u', 'University'),
    ('t', 'Training'),    
)


class Profile(models.Model):

    name =              models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description =       models.TextField(blank=True)
    image =             models.URLField(max_length=200)
    updated =           models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return (self.name)


class Skill(models.Model):

    name =     models.CharField(max_length=100)
    icon =     models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField ("Position", blank=True,null=True)

    def __str__(self):
        return self.name

    def __unicode__(self): 
        return (self.name)

    class Meta:
        ordering = ['position'] 



class Experience(models.Model):
    
    user =              models.ForeignKey('Profile',related_name='user', on_delete=models.CASCADE)
    type_experience =   models.CharField(max_length=1,default='c', choices=TYPE_EXPERIENCE)
    title =             models.CharField(max_length=100)
    company =           models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    logo =              models.URLField(max_length=200)
    date =              models.CharField(max_length=50)
    description =       models.TextField(blank=True)
    skills =            models.ManyToManyField(Skill)
    position =          models.PositiveSmallIntegerField ("Position", blank=True,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['position']
    

    def __unicode__(self):
        return (self.title)    


class Social(models.Model):
    
    user = models.ForeignKey('Profile',related_name='user', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200, blank=True)
    icon = models.CharField(max_length=100)

    def __unicode__(self): 
        return (self.name)

    def __str__(self):
        return self.name    




class Education(models.Model):

    user =              models.ForeignKey('Profile',related_name='user', on_delete=models.CASCADE)
    name =              models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    icon =              models.CharField(max_length=100)
    link =              models.URLField(max_length=200, blank=True)
    type_education =    models.CharField(max_length=1, default='t', choices=TYPE_EDUCATION)
    position =          models.PositiveSmallIntegerField ("Position", blank=True,null=True)

    def __unicode__(self): 
        return (self.name)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name        



class Post(models.Model):

    name =    models.CharField(max_length=100)
    email =   models.EmailField(max_length = 254) 
    message = models.TextField()