# Create your views here.
# views.py
from django.shortcuts import render, redirect

# "Base de datos" en memoria
TASKS = []


def task_list(request):
    context = {
        "tasks": TASKS
    }
    return render(request, "tasks/task_list.html", context)


def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            TASKS.append({
                "title": title,
                "completed": False
            })
        return redirect("task_list")

    return render(request, "tasks/task_form.html")


def task_edit(request, index):
    if index < 0 or index >= len(TASKS):
        return redirect("task_list")

    task = TASKS[index]

    if request.method == "POST":
        task["title"] = request.POST.get("title")
        task["completed"] = True if request.POST.get("completed") else False
        return redirect("task_list")

    return render(request, "tasks/task_form.html", {
        "task": task,
        "index": index
    })