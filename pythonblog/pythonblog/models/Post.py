from django.db import models
from django.urls import reverse


# Post Class로만 접근이 가능
class PostgManager(models.Manager):

    def public(self):  # self -> 클래스로부터 만들어진 객체 자기자신
        return self.filter(is_public=True)


class Post(models.Model):

    objects = PostgManager()

    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()
    image = models.ImageField(
        blank=True,
        null=True,
    )
    is_public = models.BooleanField(
        default=True
    )

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

    def get_image_url(self):
        if self.image:
            return self.image.url
        return "http://placehold.it/300x200"
