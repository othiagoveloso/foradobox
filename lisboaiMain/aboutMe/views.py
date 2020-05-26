from django.shortcuts import render
from rest_framework import viewsets
from .models import Profile,Experience, Skill, Education, Social, Certifications
from .serializers import ProfileSerializer,ExperienceSerializer, SkillSerializer, EducationSerializer, SocialSerializer, CertificationSerializer


# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer 

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer       

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = EducationSerializer  

class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer 

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certifications.objects.all()
    serializer_class = CertificationSerializer 



