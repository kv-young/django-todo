from django.urls import path
from todolist import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "tasks/<int:task_id>/toggle/",
        views.toggle_completed,
        name="toggle",
    ),
    path("tasks/<int:task_id>/update/", views.update, name="update"),
    path("tasks/<int:task_id>/delete/", views.delete, name="delete"),
]
