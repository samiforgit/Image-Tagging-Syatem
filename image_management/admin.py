from django.contrib import admin

# Register your models here.
from .models import Tag, ImageAnalise

admin.site.register(Tag)
admin.site.register(ImageAnalise)
