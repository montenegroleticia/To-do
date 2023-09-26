from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.SignIn.as_view(), name='signin'),
]
