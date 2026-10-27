from django.urls import path
from todolist import views

urlpatterns = [
    path("", views.home, name="home"),
]
