from django.db import models


class Comment(models.Model):

    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    content = models.TextField()

    def __str__(self):
        return self.content
