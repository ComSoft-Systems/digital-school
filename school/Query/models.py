from django.db import models
from django.utils import timezone
from dependencies.models import Fee_Category , Class , School , Section , Family
from django.urls import reverse

class Entry_data(models.Model):
    Query_code = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    Name = models.CharField(max_length=30, verbose_name="Name")
    father_name = models.CharField(max_length=30, verbose_name="Father")
    Address = models.CharField(max_length=30)
    last = models.ForeignKey(Class, on_delete= models.CASCADE, default=1)
    Previous_school = models.ForeignKey(School, on_delete= models.CASCADE, default=1)
    Addmission_required = models.ForeignKey(Class, on_delete= models.CASCADE, related_name='required', default=1)
    Test_performed = models.BooleanField()
    Suggested_class = models.ForeignKey(Class, on_delete= models.CASCADE, related_name='suggested')
    test_teacher = models.CharField(max_length=30)
    date_of_test = models.DateField()
    Fee_type = models.ForeignKey(Fee_Category, on_delete= models.CASCADE)
    Contact = models.CharField(max_length=20)
    def	get_absolute_url(self):
        return reverse('entry_detail',args=[self.Query_code])
    def __str__(self):
        return self.Query_code
    class Meta:
        ordering = ('Query_code',)
        index_together = (('Query_code', 'Name'),)

    class Entry_dataManager(models.Manager):				
        def	get_queryset(self):
            return super(Entry_dataManager,self).get_queryset().filter(self.Query_code)

					
