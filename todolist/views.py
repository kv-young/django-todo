from django.shortcuts import render, redirect, get_object_or_404
from todolist.models import Task
from django.core.paginator import Paginator


from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from todolist.models import Task


def home(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()

        if title:
            Task.objects.create(title=title)

        return redirect("home")

    # Search
    search_query = request.GET.get("q", "").strip()

    # Status filter
    status = request.GET.get("status", "all")

    tasks = Task.objects.all().order_by("-created_at")

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if status == "completed":
        tasks = tasks.filter(completed=True)
    elif status == "pending":
        tasks = tasks.filter(completed=False)

    # Pagination
    paginator = Paginator(tasks, 5)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        "todolist/tasks.html",
        {
            "tasks": page_obj,
            "page_obj": page_obj,
            "status": status,
            "search_query": search_query,
        },
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


def detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)  
    
    return render(request, "todolist/task_detail.html", {"task": task})
