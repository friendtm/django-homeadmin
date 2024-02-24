from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('create-task', views.create_task, name='create_task'),
    path('delete-task/<int:id>', views.delete_task, name="delete_task"),
    path('create-prod', views.create_prod, name="create_prod"),
    path('delete-prod/<int:id>', views.delete_prod, name="delete_prod"),
    path('register', views.register_user, name="register_user"),
]