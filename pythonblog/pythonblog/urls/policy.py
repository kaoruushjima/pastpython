from django.urls import path, include

from pythonblog.views import *


urlpatterns = [
    path('terms/', terms, name="terms"),
    path('privacy/', privacy, name="privacy"),
    path('disclaimer/', disclaimer, name="disclaimer"),
]
