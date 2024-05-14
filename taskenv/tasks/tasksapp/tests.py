from django.test import TestCase
from . models import Task
from django.urls import reverse
from django.contrib.auth.models import User


class TaskTest(TestCase):
    def setUp(self):
       self.user =  User.objects.create(username="testUser", email="test@user.com")
       self.user.set_password('a1b2c3d4')
       self.user.save()
       self.task = Task.objects.create(title="Tarefa", description="teste", completed=0, user=self.user)
       self.client.force_login(self.user)

    def test_create_task(self):
        response = self.client.post(reverse('create_task'), {"title": "Tarefa Teste", "description":" TESTE", "completed":"0"})
        self.assertEqual(Task.objects.last().title, "Tarefa Teste")

    def test_edit_task(self):
        response = self.client.post(reverse('update_task', kwargs={'id': self.task.id}), {"title": "Teste editado", "description":" TESTE", "completed":"0"})
        self.assertEqual(Task.objects.get(id=self.task.id).title, "Teste editado")

    def test_delete_task(self):
        response = self.client.get(reverse('delete_task', kwargs={'id': self.task.id}))
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
