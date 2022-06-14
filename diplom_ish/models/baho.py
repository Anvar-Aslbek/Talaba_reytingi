from django.db import models
from .talaba import Student
from .fan import Subject
from model_utils.fields import StatusField
from model_utils import Choices


class Baho(models.Model):
    talaba_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    fan_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    STATUS = Choices('2', '3', '4', '5')
    baho = StatusField()

    def __str__(self):
        t = Baho.objects.filter(talaba_id=self.talaba_id)
        s = 0
        cnt = 0
        cnt2=0
        cnt3=0
        cnt4=0
        cnt5=0
        for i in t:
            cnt += 1
            if i.baho == '2':
                cnt2+=1
            elif i.baho == '3':
                cnt3+=1
            s += int(i.baho)
        if cnt2 >= 3:
            res = f'{cnt2}ta 2baho kursdan kursga qoladi'
        elif 100*(cnt3+cnt2)/cnt>=30:
            res = f'{"%.2f"%(100*(cnt3+cnt2)/cnt)}% 3baho, stipendiya olmaydi'
        elif cnt*5!=s:
            res = f'{100*(cnt3+cnt2)/cnt}% 3baho, stipendiya oladi'
        else:
            res = '5 lik stipendiya oladi'
        student = Student.objects.get(id = self.talaba_id.id)
        student.holat = res
        student.save()
        return f"{self.talaba_id}ni {self.fan_id}idan bahosi {self.baho}"
