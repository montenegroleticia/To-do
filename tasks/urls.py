from django.urls import path

from . import views

urlpatterns = [
    path('health/', views.health),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name="new-task"),
]
