from django.db import models
from django.urls import reverse


class Comment(models.Model):

    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    # 같은 앱(appolication)이라면, from .post import Post 라고 부를 필요 없이, "Post"라고 기재를 해도 되며, 더 좋은 코드이다.

    content = models.TextField()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse(
            "posts:detail",
            kwargs={
                "post_id": self.post.id,
            }
        ) + "#comment-" + str(self.id)
