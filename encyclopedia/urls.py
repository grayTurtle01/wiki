from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.wiki),
    path("wiki/search_wiki", views.search_wiki, name="search_wiki"),
    path("wiki/create_wiki", views.create_wiki, name="create_wiki"),
    path("wiki/save_wiki", views.save_wiki, name="save_wiki"),
    path("wiki/edit_wiki/<str:title>", views.edit_wiki, name="edit_wiki"),
    path("wiki/update_wiki/<str:title>", views.update_wiki, name="update_wiki"),

    path("wiki/<str:title>", views.show_wiki, name="show_page"),
]
