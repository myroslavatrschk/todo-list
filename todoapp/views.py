from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from todoapp.models import Task, Tag


def index(request):
    tasks = Task.objects.order_by("completed", "-created")
    context = {"tasks": tasks, "tags": Task.tags}

    return render(request, "todoapp/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todoapp:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todoapp:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todoapp:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todoapp:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todoapp:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todoapp:tag-list")


class TaskStatusView(generic.View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()

        return HttpResponseRedirect(reverse_lazy("todoapp:index"))
