from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.wiki),
    path("wiki/search_wiki", views.search_wiki, name="search_wiki"),
    path("wiki/create_wiki", views.create_wiki, name="create_wiki"),

    path("wiki/<str:title>", views.show_wiki, name="show_page"),
]
