from django.db import models



class Student(models.Model):
    s_id = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    dpt = models.CharField(max_length=50)
    phn = models.CharField(max_length=11)


class Teacher(models.Model):
    t_id = models.CharField(max_length=10)
    t_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    dpt = models.CharField(max_length=50)
