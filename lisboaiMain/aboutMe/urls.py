from django.contrib import admin
from django.urls import path, include
from lisboaiMain.aboutMe import views
from lisboaiMain.aboutMe.views import ProfileViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)



urlpatterns = [
   
    path('', include(router.urls)),

] 