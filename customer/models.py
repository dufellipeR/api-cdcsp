from django.db import models

# Create your models here.

class Customer(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=20)