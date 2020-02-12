from django.db import models
from dependencies.models import Fee_Category , Class , School , Section , Family

class Gr(models.Model) :
    gr_number = models.IntegerField(auto_created=True , unique = True , primary_key = True)
    query_code = models.IntegerField(unique = True)
    name = models.CharField(max_length = 200)
    picture = models.FileField(upload_to = 'images')
    family_code = models.ForeignKey(Family , on_delete= models.CASCADE)
    fee_catogery_code = models.IntegerField()
    class_of_admission = models.CharField(max_length = 15)
    session_of_admission = models.IntegerField()
    current_class = models.CharField(max_length = 15)
    current_session = models.IntegerField()
    admission_date = models.DateField()
    last_school = models.CharField(max_length = 200)
    religion = models.CharField(max_length=20)
    def __str__(self):
        return  self.name
    class Meta:
        ordering = ('name',)
        verbose_name = 'Gr'
        verbose_name_plural = 'Grs'
    def get_absolute_url(self):
        return reverse('Gr:GrNumbers_In_Order',args=[self.gr_number])

        