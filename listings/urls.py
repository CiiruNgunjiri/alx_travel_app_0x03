from django.urls import path
from . import views

urlpatterns = [
    # Example endpoint, you can replace or extend this later
    path('', views.index, name='index'),
]
