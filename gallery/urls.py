from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# root URL patterns
urlpatterns = [
                  path('', include('authentication.urls')),
                  path('', include('images.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Media root when DEBUG is True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# error handlers
handler404 = "images.errors.page_not_found_view"
