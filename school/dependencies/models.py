from django.db import models

class Fee_Category(models.Model):
    fee_category_code = models.IntegerField(auto_created= True, unique = True , primary_key = True)
    fee_category_name = models.CharField(max_length=100)
    percent = models.FloatField()
    amount = models.IntegerField()
    def __str__(self):
        return self.fee_category_name

class Classe(models.Model):
    class_code = models.IntegerField(auto_created= True, unique = True, primary_key= True)
    class_name = models.CharField(max_length = 200)
    remarks = models.TextField()
    def __str__(self):
        return self.class_name

class School(models.Model):
    school_code = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    school_name = models.CharField(max_length=200)
    school_area = models.CharField(max_length=200)
    remarks = models.TextField()
    def __str__(self):
        return self.school_name

class Section(models.Model):
    sect_code = models.IntegerField(auto_created= True, unique=True, primary_key=True)
    sect_name = models.CharField(max_length=200)
    remarks = models.TextField()
    def __str__(self):
        return self.sect_name

class Family(models.Model):
    family_code = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    family_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    father_cell_no = models.IntegerField(unique=True, max_length=11)
    mother_cell_no = models.IntegerField(unique=True, max_length=11)
    address = models.CharField(max_length=200)
    remarks = models.TextField()
    def __str__(self):
        return self.family_name
