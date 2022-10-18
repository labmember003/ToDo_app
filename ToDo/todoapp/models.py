from email.policy import default
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class ToDoList(models.Model):
    todoTitle=models.CharField(blank=False,max_length=120,default="New Task")
    todoDescription=models.TextField(blank=True,default="")
    def __str__(self):
        return str(self.todoTitle)
