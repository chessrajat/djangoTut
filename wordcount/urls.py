from django.urls import path
from . import views

urlpatterns = [
    path('wordcount', views.word_count, name="wordcount"),
    path('count', views.count, name="count"),

]