"""WeatherApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Wapp.views import update_database
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Wapp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('Wapp.urls')),
    path('', include('Wapp.urls'), name='home'),
    path('update_database/', update_database)
]
