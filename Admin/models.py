from django.db import models
from api.models import *



class help(models.Model):
    ids = models.CharField(max_length=255,null= False)
    Messsage = models.CharField(max_length=255,null= False)
    send = models.CharField(max_length =255, default="We will Look Into it")
    class Meta:
        db_table = 'Help'
    def _str_(self):
        return self.ids