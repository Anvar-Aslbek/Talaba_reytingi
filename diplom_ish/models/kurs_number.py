from django.db import models

class Course_number(models.Model):
    name = models.IntegerField()

    def __str__(self):
        return f'{self.name}'