from django.shortcuts import render, redirect, get_object_or_404
from todolist.models import Task


def home(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(title=title)
            return redirect("home")
    status = request.GET.get("status", "all")
    tasks = Task.objects.all().order_by("-created_at")
    if status == "completed":
        tasks = tasks.filter(completed=True)
    if status == "pending":
        tasks = tasks.filter(completed=False)
    return render(
        request, "todolist/tasks.html", {"tasks": tasks, "status": status}
    )


def toggle_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()

    return redirect("home")


def update(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        completed = "completed" in request.POST

        task.title = title
        task.completed = completed
        task.save()

        return redirect("home")
    return render(request, "todolist/update.html", {"task": task})


def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect("home")

    return render(request, "todolist/delete_confirmation.html", {"task": task})   
