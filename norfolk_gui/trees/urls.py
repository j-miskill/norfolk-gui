import views
from django.urls import path, include


url_patterns = [
    path("", views.home_view, name="home"),
    path("/map", views.TreeView, name="map"),
]

