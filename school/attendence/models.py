from django.db import models
from student_information.models import *
from dependencies.models import *

# Create your models here.
class attendence(models.model):
    attendence_ID = models.AutoField(primary_key = True , unique = True)
    Session = models.ForeignKey(Session, on_delete = models.CASCADE, related_name= 'homework_class')
    classes = models.ForeignKey(Class, on_delete = models.CASCADE, related_name= 'homework_class')
    sections = models.ForeignKey(Section, on_delete = models.CASCADE, related_name= 'homework_class')
    gr-no = models.ForeignKey(Gr, on_delete = models.CASCADE, related_name= 'homework_class')
    attendence = models.BooleanField()
    date = models.DateField() 