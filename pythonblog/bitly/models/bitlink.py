from django.contrib.auth.models import User
from django.db import models


class Bitlink(models.Model):

    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    original_url = models.URLField()
    shorten_hash = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    # TimeStamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.original_url
