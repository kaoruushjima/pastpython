from django.views.generic import View

from pythonblog.models import Post


class PostBaseView(View):
    model = Post
