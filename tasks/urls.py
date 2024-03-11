from django.urls import path

from tasks.views import (
    TaskListView, TaskCreateView,
    TaskUpdateView, TaskDeleteView,
    TagListView, TagCreateView,
    TagUpdateView, TagDeleteView,
    complete_task, undo_task
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path(
        "complete_task/<int:task_id>/",
        complete_task,
        name="complete_task"
    ),
    path(
        "undo_task/<int:task_id>/",
        undo_task,
        name="undo_task"
    ),
]

app_name = "tasks"
