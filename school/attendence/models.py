from django.db import models
from student_information.models import *
from dependencies.models import *


# Create your models here. 
class SaveAttendence(models.Model):
    attendence_ID = models.AutoField(primary_key = True , unique = True)
    attendence_date = models.DateField()
    attendence_name = models.ForeignKey(Gr, on_delete = models.CASCADE)
    attendence_father = models.ForeignKey(Family, on_delete = models.CASCADE)
    attendence_classes = models.ForeignKey(Class, on_delete = models.CASCADE)
    attendence_sections = models.ForeignKey(Section, on_delete = models.CASCADE)
    attendence_checkBox = models.CharField(max_length = 20)


class SelectAttendence(models.Model):
    select_attendence_ID = models.AutoField(primary_key = True , unique = True)
    name = models.ForeignKey(Gr, on_delete = models.CASCADE)
    father = models.ForeignKey(Family, on_delete = models.CASCADE)
    classes = models.ForeignKey(Class, on_delete = models.CASCADE)
    sections = models.ForeignKey(Section, on_delete = models.CASCADE)
    checkBox = models.ForeignKey(SaveAttendence, on_delete = models.CASCADE)
     