from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.apps import apps
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from image_management.apps import ImageManagementConfig
from image_management.models import ImageAnalise, Tag


class ImageManagementConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ImageManagementConfig.name, 'image_management')
        self.assertEqual(apps.get_app_config('image_management').name, 'image_management')


class UserTests(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username='admin@gmail.com',
            email='admin@gmail.com',
            password='admin123',
        )
        self.client.force_authenticate(self.superuser)
        self.image_file = SimpleUploadedFile(name='test_image.jpg',
                                             content=open('media/images/test_image.jpg', 'rb').read(),
                                             content_type='image/jpeg')

    def test_add_tag(self):
        """ Test create a tag."""
        self.data = {
            "name": "TAG1"
        }
        self.url = reverse('add-tags')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_upload_image(self):
        """ Test upload a image."""
        self.data = {
            "name": "Town",
            "image": self.image_file,
        }
        self.url = reverse('upload-image')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_tag_image(self):
        """ Test tag a image."""
        image_obj = ImageAnalise(name='city',image=self.image_file)
        image_obj.save()

        tag_obj = Tag(name='Tag1')
        tag_obj.save()
        self.data = {
            "tag": tag_obj.pk
        }
        self.url = reverse('tag-image', kwargs={'pk': image_obj.pk})
        response = self.client.patch(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_image_by_tag_name(self):
        """ Test search a image by tag name."""
        self.url = reverse('search-image-by-tag', kwargs={'tag': 'invalid_tag'})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

