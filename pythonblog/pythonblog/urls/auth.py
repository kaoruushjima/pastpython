from django.urls import path, include

from pythonblog.views.auth import *


app_name = 'auth'
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('my/page/', mypage, name="mypage"),
]
