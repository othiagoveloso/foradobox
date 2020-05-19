from django.urls import path, include
from lisboaiMain.core import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
 
    path('summernote/', include('django_summernote.urls')),  
    path('', views.index, name='index'),
    path('categoria/<str:nameUrl>', views.pageArticle, name='pageArticle'),
    path('article/<str:slug>', views.post, name='post'),
    path('about/', views.aboutUs, name='aboutUs'),
    path('contact/', views.contact, name='contact'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)