"""
URL configuration for yummy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home.views import index
from django.conf.urls.static import static
from account.views import UserLogin, UserRegister, logout
from home.views import thanks
urlpatterns = [
    path('admin/', admin.site.urls),
    path('thanks/', thanks, name='thanks'),
    path('manager/', include('manager.urls')),

    path('', index, name='index'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register/', UserRegister.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
