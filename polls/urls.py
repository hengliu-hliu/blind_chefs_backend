from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("my_view", views.my_view,
         name="my_view"),
    path("test", views.raw_post_view, name="raw_post_view")
]