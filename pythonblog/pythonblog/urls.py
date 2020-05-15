"""pythonblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#MVC 
#M_MODEL : DB ( DATA ) & BUSINESS LOGIC ( * ) -> 더 무겁게
#V_VIEW : HTML, CASS, ... => Template/Client
#C_CONTROLLER : VIEW, MODEL 이어주는   -> 더 가볍게 ( 즉, 기능이 Controller => Model ..)
from django.contrib import admin
from django.urls import path

from pythonblog.views import home


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home), 

]