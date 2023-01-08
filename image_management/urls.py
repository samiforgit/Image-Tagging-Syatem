from django.urls import path
from .views import *


urlpatterns = [
    path('upload-image/', UploadImage.as_view(), name='upload-image'),
    path('add-tags/', AddTags.as_view(), name='add-tags'),
    path('tag-image/<int:pk>/', TagImage.as_view(), name='tag-image'),
    path('search-image-by-tag/<str:tag>/', SearchImageByTag.as_view(), name='search-image-by-tag'),
]