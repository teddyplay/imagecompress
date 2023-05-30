from rest_framework import serializers
from iamge_compressor.models import ImageCompressor


class ImageCompressorSerializer(serializers.ModelSerializer):
    class Meta:
        model =ImageCompressor
        fields = (
            "title",
            "image",
        )
        read_only_fields = fields
