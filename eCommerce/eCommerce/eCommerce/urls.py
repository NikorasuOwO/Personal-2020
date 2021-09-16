
from django.contrib import admin
from django.urls import path, include
import Store.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(Store.urls))
]
