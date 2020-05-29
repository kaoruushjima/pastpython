from django.views.generic.list import ListView

from .base import PostBaseView


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"

    # 3. ListView, get_paginate_by
    def get_paginate_by(self, queryset):
        return self.request.GET.get("per", 5)

    # 2. get_queryset
    # def get_queryset(self):
    #     queryset = super(PostListView, self).get_queryset()
    #     page = self.request.GET.get("page", 1)
    #     per = self.request.GET.get("per", 5)
    #     paginator = Paginator(queryset, per)
    #     posts = paginator.page(page)
    #     return posts // or paginator.page(page)
    #
    # 1. get_context_data
    # def get_context_data(self, **kwargs):
    #     context = super(PostListView, self).get_context_data(**kwargs)
    #     page = self.request.GET.get("page", 1)
    #     per = self.request.GET.get("per", 5)
    #     # [self.context_object_name] => posts 라고 생각
    #     paginator = Paginator(context[self.context_object_name], per)
    #     context[self.context_object_name] = paginator.page(page)
    #     return context
