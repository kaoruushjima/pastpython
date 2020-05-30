from django.urls import path, include

from bitly.views import *


app_name = 'bitly'
urlpatterns = [
    path('new/', BitlinkCreateView.as_view(), name="create"),

]
