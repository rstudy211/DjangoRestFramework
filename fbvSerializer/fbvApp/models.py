from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name  = models.CharField(max_length=25)
    score = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return str(self.id)+self.name+str(self.score)
    