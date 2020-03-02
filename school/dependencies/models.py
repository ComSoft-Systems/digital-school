from django.db import models

class Class(models.Model):
    class_code = models.IntegerField(auto_created= True, unique = True, primary_key= True)
    class_name = models.CharField(max_length = 200)
    remarks = models.TextField()
    def __str__(self):
        return self.class_name

class Family(models.Model):
    family_code = models.IntegerField(auto_created=True,primary_key = True,unique = True)
    surname = models.CharField(unique = True , max_length = 200)
    father_name = models.CharField(max_length = 200)
    ph_no_father = models.CharField(max_length = 200)
    mother_name = models.CharField(max_length = 200)
    ph_no_mother = models.CharField(max_length = 200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.surname       

class Fee_Category(models.Model):
    fee_category_code = models.IntegerField(auto_created= True, unique = True , primary_key = True)
    fee_category_name = models.CharField(max_length=100)
    percent = models.FloatField()
    amount = models.IntegerField()
    def __str__(self):
        return self.fee_category_name



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
        


class Session(models.Model):
    session_code = models.IntegerField(auto_created=True, primary_key= True, unique= True)
    session_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.session_name

class Religion(models.Model):
    religion_code = models.IntegerField(auto_created=True, primary_key= True, unique= True)
    religion = models.CharField(max_length = 200)
    def __str__(self):
        return self.religion

class Subject(models.Model):
    subject_code = models.IntegerField(auto_created=True, primary_key= True, unique= True)
    subjects = models.CharField(max_length = 200)
    def __str__(self):
        return self.subjects