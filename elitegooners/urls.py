
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include

from . import settings
from .views import hello_elites

urlpatterns = [
    path("admin/", admin.site.urls),
    path('hi/', hello_elites),
    path('', include("elites.urls")),
]
# Add static files URL patterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)