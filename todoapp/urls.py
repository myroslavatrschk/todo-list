from django.urls import path

from todoapp.views import index

urlpatterns = [
    path("", index, name="index"),
]
