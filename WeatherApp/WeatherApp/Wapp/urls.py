
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name="home2"),
    path('404_error/', views.notfound, name="notfound")
]
