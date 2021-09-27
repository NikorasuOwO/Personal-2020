from django.urls import path
from . import views
urlpatterns = [
    path('', views.form1, name="form1"),
    path('form1/', views.form1, name="form1"),
    path('thanks/', views.thanks, name="thanks")
]