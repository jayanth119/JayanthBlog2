# urls.py

from django.urls import path 
from .views import all_projects

urlpatterns = [
    path('', all_projects, name="all_projects"),
]
