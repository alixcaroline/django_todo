from django.urls import path
from . import views


urlpatterns = [
    # Add task
    path("addTask/", views.addTask, name="addTask"),
    # Mark task as done
    path("mark_as_done/<int:pk>/", views.mark_as_done, name="mark_as_done"),
    # Mark task as not done
    path("mark_as_not_done/<int:pk>/", views.mark_as_not_done, name="mark_as_not_done"),
    # Edit task
    path("edit_task/<int:pk>/", views.edit_task, name="edit_task"),
]
