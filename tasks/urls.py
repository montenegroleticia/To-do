from django.urls import path

from . import views

urlpatterns = [
    path('health/', views.health),
    path('', views.taskList, name='task-list')
]
