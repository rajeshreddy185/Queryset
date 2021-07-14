from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.IntegerField(unique=True, null = False)
    city = models.CharField(max_length=50)
    marks = models.IntegerField()
    passed_out = models.DateField()
