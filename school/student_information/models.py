from django.db import models
from dependencies.models import *
from Query.models import *
from django.urls import reverse


class Gr(models.Model):
    gr_number = models.IntegerField(auto_created=True , unique = True , primary_key = True)
    query_code = models.ForeignKey(Entry_data , on_delete= models.CASCADE , unique = True)
    name = models.CharField(max_length = 200)
    picture = models.FileField(upload_to='images/%Y/%m/%d',blank=True)
    family_code = models.ForeignKey(Family , on_delete= models.CASCADE)
    fee_category_code = models.ForeignKey(Fee_Category , on_delete= models.CASCADE)
    class_of_admission = models.ForeignKey(Class , on_delete= models.CASCADE , related_name= 'admission_class')
    session_of_admission = models.ForeignKey(Session , on_delete= models.CASCADE , related_name= 'session_of_admission')
    current_class = models.ForeignKey(Class , max_length = 15 , on_delete= models.CASCADE , related_name= 'current_class')
    current_session = models.ForeignKey(Session , on_delete= models.CASCADE , related_name= 'current_session')
    admission_date = models.DateField()
    last_school = models.ForeignKey(School , on_delete = models.CASCADE)
    religion = models.ForeignKey(Religion,on_delete = models.CASCADE)
    date_of_birth = models.DateField()
    def get_absolute_url(self):
        return reverse('gr_detail',args=[self.gr_number])
    def __str__(self):
        return str(self.gr_number)
    class Meta:
        ordering = ('gr_number',)
        index_together = (('gr_number', 'name'),)
        verbose_name = 'Gr'
        verbose_name_plural = 'Grs'

    class GrManager(models.Manager):
        def get_queryset(self):
            return super(GrManager,self).get_queryset().filter(self.gr_number)
