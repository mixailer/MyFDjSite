from django.contrib import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

