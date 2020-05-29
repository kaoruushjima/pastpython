from django.views.generic.detail import DetailView

from .base import PostBaseView


class PostDetailView(PostBaseView, DetailView):
    template_name = "posts/detail.html"
    # context_object_name = "object" ("post")
    # 명시적으로 지정하지 않으면  object로 부를수도 있고 post(model 이름에서 소문자로 바꾼)로 자동으로 template에서 부를 수도 있다.
    # List는 사동으로 안되는데 detail을 자동으로 된다.
