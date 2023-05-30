from django.urls import path
from iamge_compressor.views import ImageCompressorView


urlpatterns = [
    path("image/", ImageCompressorView.as_view(), name="image-list")
]