from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)



