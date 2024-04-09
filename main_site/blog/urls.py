
from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
from .views import home, post,category,main , about  
urlpatterns = [
    path('', main, name= "main" ),
    path('home/', home , name= "home" ),
   path('blog/<slug:url>/', post, name='post') , 
    path('category/<slug:url>',category), 
    path('Jayanth' ,about , name="Jayanth") , 
]
