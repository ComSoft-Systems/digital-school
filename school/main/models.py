from django.db import models

class UserType(models.Model):
    TypeCode = models.IntegerField(primary_key = True , unique = True , auto_created = True)
    UserType = models.CharField(max_length = 50)
    def __str__(self):
        return self.UserType

class UserProfile(models.Model):
    UserCode = models.IntegerField(primary_key = True , unique = True , auto_created = True)
    UserType = models.ForeignKey(UserType,on_delete = models.CASCADE)
    Name = models.CharField(max_length = 50)
    Father = models.CharField(max_length = 50)
    Address = models.CharField(max_length = 200)
    Mobile = models.CharField(max_length = 11)
    Email = models.EmailField()
    Password = models.CharField(max_length = 25)
    def __str__(self):
        return self.Name
    def get_absolute_url(self):
        return reverse('search',args=[self.UserType])
