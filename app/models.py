from django.db import models
from django.core.validators import FileExtensionValidator

class Counter(models.Model):
    count = models.IntegerField(default=0)

class Post(models.Model):
        image = models.FileField(upload_to='', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp', 'mp4', 'webm'], 'Not a common image or video format.')], null=True)