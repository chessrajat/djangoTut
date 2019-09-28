
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('log_out', views.log_out, name="log_out"),
    path('destinations', views.destination, name="destination")
]

