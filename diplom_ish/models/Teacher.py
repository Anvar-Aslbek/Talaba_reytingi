from pyexpat import model
from django.db import models
from .kafedra import Kafedra


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    tel_number = models.CharField(max_length=100)
    kafedra_id = models.ForeignKey(Kafedra, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name