from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=25)

class Employee(models.Model):
    Full_Name = models.CharField(max_length=50)
    Emp_code = models.CharField(max_length=3)
    Mobile_No = models.CharField(max_length=13)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

