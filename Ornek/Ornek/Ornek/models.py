from django.db import models

class Student(models.Model):
    Id=models.AutoField(primary_key=True)
    Model=models.CharField(max_length=50)
    FinalGrade = models.DecimalField(max_digits=5,decimal_places=2)
    CreatedAt =models.DateTimeField(auto_now=True)