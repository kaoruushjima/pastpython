from django.shortcuts import render

from pythonblog.models import Post


def list(request):
    return render(
        request,
        "posts/list.html",
        {
            "posts": Post.objects.all(),
        }
    )
