from django.shortcuts import render

from todoapp.models import Task


def index(request):
    tasks = Task.objects.order_by("completed", "-created")
    context = {"tasks": tasks, "tags": Task.tags}

    return render(request, "todoapp/index.html")
