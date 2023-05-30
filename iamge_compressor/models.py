from django.db import models
from PIL import Image
from django.core.files.base import ContentFile


class ImageCompressor(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=("Заголовок"))
    image = models.ImageField(upload_to="iamge_compressor", null=False, blank=False, verbose_name=("Изобрадение"))

    def __str__(self) -> str:
        return str(self.title)


    class Meta:
        db_table = "image__compress"
        verbose_name = ("Изобпажение")
        verbose_name_plural = ("Изобпажения")

