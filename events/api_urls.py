from django.urls import path

from .api_views import (
    api_list_conferences,
    api_get_locations,
    api_show_conference,
    api_show_location,
)


urlpatterns = [
    path("conferences/", api_list_conferences, name="api_list_conferences"),
    path(
        "conferences/<int:id>/",
        api_show_conference,
        name="api_show_conference",
    ),
    path("locations/", api_get_locations, name="api_get_locations"),
    path("locations/<int:id>/", api_show_location, name="api_show_location"),
]
