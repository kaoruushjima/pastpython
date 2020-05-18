from django.urls import path, include

from pythonblog.views.posts import *


app_name = 'posts'
urlpatterns = [
    path('', list, name="list"),
    path('<int:post_id>/', detail, name="detail"),
    path('create/', create, name="create"),
    path('new/', new, name="new"),
    path('<int:post_id>/edit/', edit, name="edit"),
    path('<int:post_id>/update/', update, name="update"),
    path('<int:post_id>/delete/', delete, name="delete"),
]
