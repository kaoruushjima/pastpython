from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from pythonblog.models import Post
from .base import PostBaseView


class PostCreateView(PostBaseView, CreateView):
    fields = [
        "title",
        "content",
        "image",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
