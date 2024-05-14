from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from tasksapp.models import Task
from django.forms.widgets import PasswordInput, TextInput

# Formulário de Criação de Usuários
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Formulário de Login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class TaskForm(ModelForm):
    class Meta:
        model = Task
        labels = {
            "title" : "Título",
            "Description" : "Descrição",
            "completed" : "Tarefa Concluída?"
        }
        fields = ['title', 'description', 'completed']
