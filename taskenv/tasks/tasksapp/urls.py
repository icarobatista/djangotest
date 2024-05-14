from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout, name="logout"),
    path('task', views.createTask, name="create_task"),
    path('task/<int:id>', views.updateTask, name="update_task"),
    path('task/<int:id>/delete', views.deleteTask, name="delete_task"),

]

