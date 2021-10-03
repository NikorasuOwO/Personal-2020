from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name="store"),
    path('store/product/<int:id>/', views.view_prod)
]