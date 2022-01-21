from customer.models import Customer
from status.models import Status
from department.models import Department
from station.models import Station
from django.db import models
from issue.models import Issue
from django.contrib.auth.models import User

# Create your models here.
class Protocol(models.Model):
  SLA_OPTIONS = [
    ('4', '4'),
    ('6', '6'),
    ('24', '24'),
    ('48', '48')
  ]

  # Fazer aplicativo

  clerk = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
  issue = models.ForeignKey(to=Issue, on_delete=models.SET_NULL, null=True )
  customer = models.ForeignKey(to=Customer, on_delete=models.SET_NULL, null=True)
  station = models.ForeignKey(to=Station, on_delete=models.SET_NULL, null=True)
  department = models.ForeignKey(to=Department, on_delete=models.SET_NULL, null=True, blank=True)
  status = models.ForeignKey(to=Status, on_delete=models.SET_NULL, null=True)
  protocol_opening = models.DateTimeField()
  protocol_link = models.CharField(max_length=255, default='No link')
  date = models.DateField()
  note = models.TextField(blank=True)
  sla = models.CharField(choices=SLA_OPTIONS, max_length=255)

  def __str__(self):
    return  self.customer.code +  ' ' + self.customer.name + ' ' +  self.issue.name  