from django.db import models

# Create your models here.
class Crud(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  mobno = models.CharField(max_length=255)
  email = models.CharField(max_length=255)