from django.db import models
from .Teacher import Teacher

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    decan_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name