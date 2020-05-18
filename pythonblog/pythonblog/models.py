from django.db import models
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "posts:detail",
            kwargs={
                "post_id": self.id
            }
        )

    def get_update_url(self):
        return reverse(
            "posts:update",
            kwargs={
                "post_id": self.id
            }
        )


class NaverPost(models.Model):

    keyword = models.CharField(
        max_length=16,
    )

    title = models.CharField(
        max_length=256,
    )

    content = models.TextField()
    thumbnail_image_url = models.URLField()
    original_url = models.URLField()

    def __str__(self):
        return self.title
