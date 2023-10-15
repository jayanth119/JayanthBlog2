"""iblogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
# from django.conf.urls.static import static
from django.conf import settings
from .views import home, post,category,main , about  
urlpatterns = [
    path('', main, name= "main" ),
    path('home/', home , name= "home" ),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category), 
    path('Jayanth' ,about , name="Jayanth") , 
    # path('like/<int:pk>',postlike , name="blog_like"),
]
