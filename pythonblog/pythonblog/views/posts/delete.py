from django.shortcuts import redirect

from pythonblog.models import Post


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect("posts:post-list")
