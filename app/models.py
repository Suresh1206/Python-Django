from django.db import models

# Create your models here.
class Student(models.Model):
    Student_id = models.CharField(max_length=10)
    Student_Name = models.CharField(max_length=50)
    Student_Branch = models.CharField(max_length=50)