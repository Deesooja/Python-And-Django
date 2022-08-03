from pickle import TRUE
from django.db import models

# Create your models here.
class All_todo(models.Model):
    id=models.IntegerField(primary_key=TRUE)
    todo=models.CharField(max_length=150)
    status=models.CharField(max_length=20, default='Not Done')

class Done_todo(models.Model):
    id=models.IntegerField(primary_key=TRUE)
    todo=models.CharField(max_length=150)
    status=models.CharField(max_length=20, default='Done')
    

class History_todo(models.Model):
    id=models.IntegerField(primary_key=TRUE)


    todo=models.CharField(max_length=150)
    status=models.CharField(max_length=20, default='Not Done')