from rest_framework import generics, status
from rest_framework.response import Response

from image_management.models import Tag, ImageAnalise
from image_management.serializer import TagSerializer, UploadImageSerializer
from image_tagging_system.permissions import IsAuthenticated


class UploadImage(generics.CreateAPIView):
    """
    Upload Image API class.
    """
    queryset = ImageAnalise.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UploadImageSerializer


class AddTags(generics.CreateAPIView):
    """
    Add Tag to the system API class.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagImage(generics.UpdateAPIView):
    """
    Tag Image API class.
    """
    queryset = ImageAnalise.objects.all()
    serializer_class = UploadImageSerializer
    permission_classes = [IsAuthenticated]


class SearchImageByTag(generics.GenericAPIView):
    """
    Search Image by class name API class.
    """
    queryset = ImageAnalise.objects.all()
    serializer_class = UploadImageSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            tag = Tag.objects.get(name=kwargs['tag'])
            if tag:
                images = ImageAnalise.objects.filter(tag=tag).values()
                if len(list(images)) == 0:
                    return Response(data={
                        'image': list(images), 'message': 'No image found by {} tag name'.format(tag)
                    }, status=status.HTTP_404_NOT_FOUND)
                return Response(data={
                    'images': list(images), 'message': 'Images found by the tag {}'.format(tag)
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'message': 'Invalid request, no tag found'}, status=status.HTTP_400_BAD_REQUEST)
