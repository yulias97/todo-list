from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


def complete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(pk=task_id)
        task.is_done = True
        task.save()
    return redirect("tasks:index")


def undo_task(request, task_id):
    if request.method == "POST":
        Task.objects.update()
        task = Task.objects.get(pk=task_id)
        task.is_done = False
        task.save()
    return redirect("tasks:index")
