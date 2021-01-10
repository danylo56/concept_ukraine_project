from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to="images")
    date = models.DateTimeField(default=None)
# Create your models here.
