from django.urls import path
from . import views

urlpatterns = [
    path("Teknik/", views.TutorialListCreate.as_view(), name="Tutorial-view-create")
]