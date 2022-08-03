from email.headerregistry import Address
from django.db import models

# Create your models here.
class registration(models.Model):
   name = models.CharField(max_length=70)
   email = models.EmailField(max_length=100)
   address = models.CharField(max_length=100)