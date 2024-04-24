from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('catalog.urls', namespace='catalog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
