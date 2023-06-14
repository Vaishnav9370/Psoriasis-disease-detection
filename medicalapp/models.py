from django.db import models

# Create your models here.

class regmodel(models.Model):
    fname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    phoneNumber=models.CharField(max_length=200,null=True)
    gen=models.CharField(max_length=200,null=True)
    adrs=models.CharField(max_length=200,null=True)
    District=models.CharField(max_length=200,null=True)

class models(models.Model):
    mlmodel=models.CharField(max_length=200,null=True)
