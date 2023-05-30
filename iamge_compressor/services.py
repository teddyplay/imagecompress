from iamge_compressor.models import ImageCompressor


class ImageCompressServices:
    __model = ImageCompressor

    @classmethod
    def get_all_or_none(cls, **filters):
        if cls.__model.objects.filter(**filters).count() != 0:
            return cls.__model.objects.filter(**filters).order_by("title")
        else:
            return cls.__model.objects.none()
