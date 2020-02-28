from django.db import models
from dependencies.models import *

# Create your models here.
class home_work(models.Model):
    homework_ID = models.IntegerField(auto_created = True, unique = True, primary_key = True)
    classes = models.ForeignKey(Class, on_delete = models.CASCADE, related_name= 'homework_class')
    sections = models.CharField(max_length = 10)
    teacher = models.CharField(max_length = 30)
    subjects = models.CharField(max_length = 20)
    chapter = models.CharField(max_length = 50)
    page = models.IntegerField()
    descriptions = models.CharField(max_length = 300)

    def __str__(self):
        return str(self.classes)