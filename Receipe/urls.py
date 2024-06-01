"""
URL configuration for Receipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Hello,name="Hello"),
    path('receipe/', receipe, name="receipe"),

    path('delete_reciepe/<id>/', delete_reciepe , name="delete_reciepe"),  # DYNAMIC URL
    path('update_reciepe/<id>/', update_reciepe , name="update_reciepe"),
    path('login_page/',login_page, name='login_page'),
    path('register/',register, name='register'),
    path('logout_page/',logout_page, name='logout_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
