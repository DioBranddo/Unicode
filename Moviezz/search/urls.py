from django.urls import path
from . import views

urlpatterns = [
    path("", views.titleSearch, name="searchByTitle"),
    path("/genre", views.genreSearch, name="searchByGenre"),
]