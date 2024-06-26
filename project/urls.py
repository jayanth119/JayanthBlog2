from django.urls import path 
from .views import all_projects
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', all_projects, name="all_projects"),
]

# Add static and media URL patterns only if DEBUG is True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
