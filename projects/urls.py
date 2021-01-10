from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts, name="all_projects"),
    path("<int:pk>/", views.post, name="project")
]
