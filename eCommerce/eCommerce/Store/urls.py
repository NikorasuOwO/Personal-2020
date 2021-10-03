from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name="store"),
    path('store/product/<int:id>/', views.view_prod),
    path('', views.redirect_store),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login")
]
