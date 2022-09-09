from django.db import models

# Create your models here.
class Sample_DB(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)