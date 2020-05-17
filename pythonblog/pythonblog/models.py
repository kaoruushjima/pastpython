from django.db import models


class Post(models.Model):

    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()


class NaverPost(models.Model):

    title = models.CharField(
        max_length=256,
    )

    content = models.TextField()
    thumbnail_image_url = models.URLField()
    original_url = models.URLField()

    def __str__(self):
        return self.title
