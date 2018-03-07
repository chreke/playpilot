from django.conf import settings
from django.db import models


class Media(models.Model):
    title = models.CharField(max_length=256)
    imdb_url = models.URLField(max_length=128)
    year = models.PositiveIntegerField()
    description = models.TextField()
    season = models.IntegerField(blank=True, null=True)
    added_by = settings.AUTH_USER_MODEL
