from django.shortcuts import redirect
from django.views.generic import View

from pythonblog.models import Post


class PostCreateView(View):

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        post = Post.objects.create(
            user=request.user,
            title=title,
            content=content,
            image=image,
        )

        # return redirect(f'/posts/{post.id}')
        return redirect(post)
