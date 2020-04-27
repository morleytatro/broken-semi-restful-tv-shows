from django.urls import path

from . import views

urlpatterns = [
    path("new", views.new_show_page),
    path("shows", views.all_shows_page),
    path("shows/<int:show_id>/edit", views.show_edit_page),
    path("shows/<int:show_id>", views.show_details_page),
    path("update_show/<int:show_id>", views.update_show),
    path("delete_show/<int:show_id>", views.delete_show)
]