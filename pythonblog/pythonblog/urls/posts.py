from django.urls import path, include

from pythonblog.views.posts import *


app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name="list"),
    path('<int:post_id>/', detail, name="detail"),
    path('create/', create, name="create"),
    path('new/', new, name="new"),
    path('<int:post_id>/edit/', edit, name="edit"),
    path('<int:post_id>/update/', update, name="update"),
    path('<int:post_id>/delete/', delete, name="delete"),

    path('<int:post_id>/comments/create/', comments_create, name="comments-create"),
    path('<int:post_id>/comments/<int:comment_id>/edit/', comments_edit, name="comments-edit"),
    path('<int:post_id>/comments/<int:comment_id>/update/', comments_update, name="comments-update"),
    path('<int:post_id>/comments/<int:comment_id>/delete/', comments_delete, name="comments-delete"),
]
