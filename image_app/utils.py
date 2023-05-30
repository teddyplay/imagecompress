from PIL import Image

def compress_image(image_instance, quality=90):
    img = Image.open(image_instance.image)
    img.save(image_instance.image.path, format='JPEG', quality=quality)

def save_image_instance(image_instance, *args, **kwargs):
    super(image_instance.__class__, image_instance).save(*args, **kwargs)
    compress_image(image_instance)
