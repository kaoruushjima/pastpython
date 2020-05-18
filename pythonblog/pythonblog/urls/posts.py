from django.urls import path, include

from pythonblog.views import *


app_name = 'posts'
urlpatterns = [
    path('', list, name="post-list"),
    path('<int:post_id>/', detail, name="post-detail"),
    path('create/', create, name="post-create"),
    path('new/', new, name="post-new"),
    path('<int:post_id>/edit/', edit, name="post-edit"),
    path('<int:post_id>/update/', update, name="post-update"),
    path('<int:post_id>/delete/', delete, name="post-delete"),
]
