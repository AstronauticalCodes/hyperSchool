from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()
    about = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField(max_length=1000)
    duration_months = models.IntegerField()
    price = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)

    def get_absolute_url(self):
        return f'../course_details/{self.id}'

    def __str__(self):
        return f"{self.title}"


class Student(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.name} {self.surname}'

# region broCodeFor Etherom
class MyCourse(models.Model):
    name =models.CharField(max_length=60)
    # meta =  models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)

class Module(models.Model):
    name =  models.CharField(max_length=60)
    # meta = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    course = models.ForeignKey(MyCourse, on_delete=models.DO_NOTHING)


class Topic(models.Model):
    name = models.CharField(max_length=60)
    # meta = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    module = models.ForeignKey(Module, on_delete=models.DO_NOTHING)


class Article(models.Model):
    name =models.CharField(max_length=60)
    context = models.TextField(max_length=1000)
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
# endregion broCodeFor Etherom

# article.objects.filter(afasd).first().topic.module.course
