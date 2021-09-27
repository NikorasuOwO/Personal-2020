
from django.contrib import admin
from django.urls import path, include
from Tests import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Tests.urls'))
]
