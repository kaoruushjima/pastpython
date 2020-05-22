from django.urls import path, include

from pythonblog.views.auth import *


app_name = 'auth'
urlpatterns = [
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', logout, name="logout"),
    path('my/page/', mypage, name="mypage"),
]
