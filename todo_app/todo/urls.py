from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('add/', views.add_task, name='add_task'),
]
