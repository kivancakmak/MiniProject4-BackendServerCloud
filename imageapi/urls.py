"""imageapi URL yollari. PDF Task 2 yollariyla birebir eslesir."""

from django.urls import path

from . import views

urlpatterns = [
    path("get/resolution", views.get_resolution, name="get_resolution"),
]
