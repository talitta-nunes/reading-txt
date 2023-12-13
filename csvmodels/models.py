
from django.db import models


# Create your models here.
class ClientForm(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=100, null=True, blank=True)
    card = models.CharField(max_length=100, null=True, blank=True)
    time = models.CharField(max_length=100, null=True, blank=True)
    hoster = models.CharField(max_length=100, null=True, blank=True)
    store = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    nature = models.CharField(max_length=100, null=True, blank=True)
    signal = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, verbose_name="")

 
