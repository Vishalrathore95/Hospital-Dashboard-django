"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup),  
    
    path('singup/', views.signup),  
    path('index/', views.index,name='index'),
    path('about/', views.about),
    path('contact/', views.contact),
    path('forgot/', views.forgot),
    path('savedata/', views.savedata, name='savedata'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('confirm/', views.comfirm),
    path('doctor/', views.doctor ,name= 'doctor'),
    path('doccard/', views.doccard),
    path('savedoc/', views.savedoc, name='savedoc'),
  
 
 
  
    
    
 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)