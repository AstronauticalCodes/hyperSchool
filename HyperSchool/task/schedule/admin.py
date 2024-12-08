from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Coursera)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
# admin.site.register(models.Article)
# admin.site.register(models.Topic)
# admin.site.register(models.Module)
# admin.site.register(models.MyCourse)