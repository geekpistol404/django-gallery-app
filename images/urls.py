from django.conf.urls.static import static
from django.urls import path

from gallery import settings
from . import views
from .views import UserListView

"""URL patterns for images app"""
urlpatterns = [
    path('', views.index, name='index'),
    path('feed/', views.images, name='feed'),
    path('upload/', views.upload, name='upload'),
    path('delete/<image_id>', views.delete, name='delete'),
    path('people', UserListView.as_view(), name='user-list'),
    path('profile/<username>', views.profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
