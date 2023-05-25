from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# importing views from views..py
from .views import detail_view
from . import views

urlpatterns = [
    path('', views.list_view),
    path('<id>', detail_view ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



