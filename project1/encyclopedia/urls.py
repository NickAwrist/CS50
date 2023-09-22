from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random/", views.randomPage, name="random_entry"),
    path("search/", views.search, name="search"),
    path("save/<str:entry>", views.saveEntry, name="save_entry"),
    path("new_entry/", views.addEntryPage, name="add_entry"),
    path("new_entry/save", views.addEntrySubmit, name="add_entry_submit"),
    path("wiki/edit/<str:entry>", views.editPage, name="edit_entry"),
    path("wiki/<str:entry>", views.toPage, name="entry")
]
