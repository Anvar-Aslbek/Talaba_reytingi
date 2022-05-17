from django.db import models
from .faculty import Faculty
from .Teacher import Teacher


class Subject(models.Model):
    name = models.CharField(max_length = 100)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

