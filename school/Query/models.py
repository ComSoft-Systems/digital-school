from django.db import models
from django.utils import timezone

class Entry_data(models.Model):
    Query_code = models.IntegerField(primary_key=True, default=1)
    Name = models.CharField(max_length=30, verbose_name="Name")
    father_name = models.CharField(max_length=30, default=1 ,verbose_name="father")
    Address = models.CharField(max_length=30, default=1)
    Test_performed = models.BooleanField(default=1)
    suggested_class = models.CharField(max_length=20, default=1)
    test_teacher = models.CharField(max_length=30, default=1)
    date_of_test = models.DateField()
    Contact = models.CharField(max_length=20, default=1)

def_str_(self):
    return self.Name