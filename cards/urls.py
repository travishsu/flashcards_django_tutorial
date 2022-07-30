from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.CardListView.as_view(template_name="cards/cards_list.html"),
        name="card-list"
    ),
]
