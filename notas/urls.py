from django.urls import path
from .views import list_notes,view,edit,create,delete

urlpatterns = [
    path("", list_notes,name="notes"),
    path("view/<int:id>", view,name="view"),
    path("edit/<int:id>", edit,name="edit"),
    path("create",create,name="create"),
    path("delete/<int:id>",delete,name="delete"),

    





]