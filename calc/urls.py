# create urls mapping for the application
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add", views.add, name="add")
]


