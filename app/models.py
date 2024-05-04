from django.db import models
from django.core.validators import FileExtensionValidator
from mimetypes import guess_type

class Counter(models.Model):
    count = models.IntegerField(default=0)

class Post(models.Model):
    image = models.FileField(upload_to='', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp', 'mp4', 'webm', 'mov'], 'Not a common image or video format.')], null=True)

    # https://docs.python.org/3/library/mimetypes.html
    def media_type_html(self):
        type_tuple = guess_type(self.image.url, strict=True)
        if (type_tuple[0]).__contains__("image"):
            return "image"
        elif (type_tuple[0]).__contains__("video"):
            return "video"