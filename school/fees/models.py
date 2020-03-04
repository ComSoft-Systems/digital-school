from django.db import models 
from student_information.models import *

class ClassFee(models.Model):
    fee_type_code = models.IntegerField(primary_key=True,auto_created=True,unique=True)
    fee_type = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    def __str__(self):
        return self.fee_type

class StFeeDefine(models.Model):
    fee_def_code = models.IntegerField(primary_key=True,auto_created=True,unique=True)
    gr_number = models.ForeignKey(Gr,on_delete=models.CASCADE)
    fee_type = models.ForeignKey(ClassFee,on_delete=models.CASCADE)
    concession_percent = models.IntegerField()
    def __str__(self):
        return '{} Fees of {}'.format(self.fee_type,self.gr_number)

class FeeRegister(models.Model):
    fee_reg_id = models.IntegerField(primary_key=True,auto_created=True,unique=True)
    gr_number = models.ForeignKey(Gr,on_delete=models.CASCADE)
    fee_types = models.ForeignKey(ClassFee,on_delete=models.CASCADE)
    fee_amount = models.CharField(max_length=5)
    month = models.CharField(max_length=2)
    due_date = models.DateField()
    paid_amount = models.CharField(max_length=5,blank=True)
    def __str__(self):
        return '{} Fees Of Month # {}'.format(self.fee_types,self.month)
    def get_absolute_url(self):
        return reverse('fee_reg_detail',args=[self.fee_reg_id])