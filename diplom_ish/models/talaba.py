from tabnanny import verbose
from django.db import models
from .kurs_number import Course_number
from .faculty import Faculty
from .fan import Subject
# from .baho import Baho

class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Ism')
    last_name = models.CharField(max_length=100, verbose_name='Familiya')
    email = models.EmailField()
    tel_number = models.CharField(max_length=100, verbose_name='phone_number')
    kurs_number_id = models.ForeignKey(Course_number, on_delete=models.CASCADE, verbose_name='kursi')
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='Fakulteti')
    fan = models.ManyToManyField(Subject)
    holat = models.CharField(max_length=100, default="bahosi qo'yilmagan")

    def holati(self):
        pass
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"
        
    