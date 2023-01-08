from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class ImageAnalise(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
