from django.shortcuts import render
from rest_framework import viewsets
from .models import Profile,Experience
from .serializers import ProfileSerializer


# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer    