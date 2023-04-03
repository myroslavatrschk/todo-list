from django.urls import path

from todoapp.views import (index,
                           TaskCreateView,
                           TaskUpdateView,
                           TaskDeleteView,
                           TaskStatusView,
                           TagListView,
                           TagCreateView,
                           TagUpdateView,
                           TagDeleteView)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/status/",
        TaskStatusView.as_view(),
        name="task-status"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]

app_name = "todoapp"
