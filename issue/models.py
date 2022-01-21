from django.db import models

# Create your models here.
class Issue(models.Model):
  name = models.CharField(max_length=255)