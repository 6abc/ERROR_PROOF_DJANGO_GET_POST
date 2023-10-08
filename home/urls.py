from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # Handle GET requests to the root URL
    path('hello', views.hello_world, name="hello_world"),  # Handle POST requests to '/hello'
]
