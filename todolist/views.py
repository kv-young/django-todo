from django.shortcuts import render
from todolist.models import Task


def home(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if not title:
            pass
        else:
            Task.objects.create(title=title)
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "todolist/tasks.html", {"tasks": tasks})
