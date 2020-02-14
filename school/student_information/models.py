from django.db import models
from dependencies.models import Fee_Category , Class , School , Section , Family
from Query.models import Entry_data
from django.urls import reverse


class Gr(models.Model):
    gr_number = models.IntegerField(auto_created=True , unique = True , primary_key = True)
    query_code = models.ForeignKey(Entry_data , on_delete= models.CASCADE)
    name = models.CharField(max_length = 200)
    picture = models.FileField(upload_to='images/%Y/%m/%d',blank=True)
    family_code = models.ForeignKey(Family , on_delete= models.CASCADE)
    fee_category_code = models.ForeignKey(Fee_Category , on_delete= models.CASCADE)
    class_of_admission = models.ForeignKey(Class , on_delete= models.CASCADE)
    session_of_admission = models.IntegerField()
    current_class = models.ForeignKey(Class , max_length = 15 , on_delete= models.CASCADE , related_name= 'current')
    current_session = models.IntegerField()
    admission_date = models.DateField()
    last_school = models.ForeignKey(School , on_delete = models.CASCADE)
    religion = models.CharField(max_length=20)
    def get_absolute_url(self):
        return reverse('gr_detail',args=[self.gr_number])
    def __str__(self):
        return str(self.gr_number)
    class Meta:
        ordering = ('name',)
        index_together = (('gr_number', 'family_code'),)
        verbose_name = 'Gr'
        verbose_name_plural = 'Grs'

    class GrManager(models.Manager):
        def get_queryset(self):
            return super(GrManager,self).get_queryset().filter(self.r_number)
