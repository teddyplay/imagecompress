from django.contrib import admin
from iamge_compressor.models import ImageCompressor


@admin.register(ImageCompressor)
class ImageAdmin(admin.ModelAdmin):
    fields = ('title', "image", )
    search_fields = ("title", )
