from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.home_view, name="home"),
    path("map/", views.TreeView.as_view(), name="map"),
]

