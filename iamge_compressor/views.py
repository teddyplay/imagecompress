from iamge_compressor.serializers import ImageCompressorSerializer
from rest_framework.generics import ListAPIView
from image_app.utils import compress_image, save_image_instance
from iamge_compressor.services import ImageCompressServices


class ImageCompressorView(ListAPIView):
    serializer_class = ImageCompressorSerializer

    def get_queryset(self):
        return ImageCompressServices.get_all_or_none()

    def perform_create(self, serializer):
        save_image_instance(serializer.save())
