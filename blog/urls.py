from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post, category, main, about

urlpatterns = [
    path('', main, name="main"),
    path('home/', home, name="home"),
    path('blog/<slug:url>/', post, name='post'),
    path('category/<slug:url>/', category, name='category'),
    path('Jayanth/', about, name="Jayanth"),
]

# Add static and media URL patterns only if DEBUG is True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
