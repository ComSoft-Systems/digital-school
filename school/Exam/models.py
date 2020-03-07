from django.db import models
from django.utils import timezone
from dependencies.models import Fee_Concession , Class , School , Section , Family, Session
from django.urls import reverse


class Exam(models.Model):
    exam_code = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    exam_session = models.ForeignKey(Session, on_delete= models.CASCADE)
    def	get_absolute_url(self):
        return reverse('exam_detail',args=[self.exam_code])
    def __str__(self):
        return str(self.exam_session)


class Semester(models.Model):
    exam_code = models.ForeignKey(Exam, on_delete= models.CASCADE)
    semester_code = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    semester_name = models.CharField(max_length=30, verbose_name="semester")
    def __str__(self):
        return self.semester_name
    def	get_absolute_url(self):
        return reverse('semester_detail',args=[self.semester_code])

class Semesterbreakup(models.Model):
    exam_code = models.ForeignKey(Exam, on_delete= models.CASCADE)
    semester_code = models.ForeignKey(Semester, on_delete= models.CASCADE)    
    semesterbreakup_code = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    semesterbreakup_name = models.CharField(max_length=30, verbose_name="semester-breakup")
    def __str__(self):
        return self.semesterbreakup_name
    def	get_absolute_url(self):
        return reverse('semesterB_detail',args=[self.semesterbreakup_code])

class Quater(models.Model):
    exam_code = models.ForeignKey(Exam, on_delete= models.CASCADE)
    semester_code = models.ForeignKey(Semester, on_delete= models.CASCADE)
    semesterbreakup_code = models.ForeignKey(Semesterbreakup, on_delete= models.CASCADE)    
    quater_code = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    quater_name = models.CharField(max_length=30, verbose_name="Quater")
    def __str__(self):
        return self.quater_name

class Assesment(models.Model):
    exam_code = models.ForeignKey(Exam, on_delete= models.CASCADE)
    semester_code = models.ForeignKey(Semester, on_delete= models.CASCADE)
    semesterbreakup_code = models.ForeignKey(Semesterbreakup, on_delete= models.CASCADE)
    quater_code = models.ForeignKey(Quater, on_delete= models.CASCADE)    
    assesment_code = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    assesment_name = models.CharField(max_length=30, verbose_name="Quater")
    def __str__(self):
        return self.assesment_name
