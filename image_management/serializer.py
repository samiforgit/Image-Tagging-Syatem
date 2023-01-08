from rest_framework.serializers import ModelSerializer
from image_management.models import Tag, ImageAnalise


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UploadImageSerializer(ModelSerializer):
    class Meta:
        model = ImageAnalise
        fields = '__all__'
