from django.urls import path

from . import views

urlpatterns = [
    path('<str:pk>/', views.show_event, name="show_event"),
    path('<str:pk>/confirmation/', views.event_confirmation, name="event_confirmation"),
    path('<str:pk>/submission-project/', views.submission_project, name="submission_project")
]