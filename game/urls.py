from django.urls import path

from . import views


urlpatterns = [
    path("cards", views.get_cards, name="get_cards"),
    path("cards/<int:id>", views.get_card_by_id, name="get_card_by_id"),
    path("test", views.raw_post_view, name="raw_post_view"),
]