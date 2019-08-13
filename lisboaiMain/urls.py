"""lisboaiMain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lisboaiMain.core import views
from lisboaiMain.aboutMe.views import ProfileViewSet
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)




urlpatterns = [
    path('admin/lisboai', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),  
    path('', views.index, name='index'),
    path('categoria/<int:id>', views.pageArticle, name='pageArticle'),
    path('article/<str:slug>', views.post, name='post'),
    path('about/', views.aboutUs, name='aboutUs'),
    path('contact/', views.contact, name='contact'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = 'Lisboai - Admin'
