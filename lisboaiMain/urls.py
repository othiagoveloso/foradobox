from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lisboaiMain.core.urls')),
    path('api/', include('lisboaiMain.aboutMe.urls')),
]





