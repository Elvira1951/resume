"""
URL configuration for resume project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from resume_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
   path('blog/', blog, name='blog'),
    path('resume/', resume, name='resume'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('download_resume/', download_resume, name='download_resume'),
    path('blogDetails/<int:id>', blogDetails, name = 'blogDetails'),
    path('comments/<int:id>', comments, name = 'comments'),
     
    
]
urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)