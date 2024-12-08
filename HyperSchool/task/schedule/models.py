from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()
    about = models.TextField(max_length=1000)


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField(max_length=1000)
    duration_months = models.IntegerField()
    price = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)


class Student(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)