from django.db import models


# Create your models here.
class Execise(models.Model):
    ExeciseID = models.IntegerField()
    name = models.CharField(max_length=25)
    rep_recommend = models.CharField(max_length=10)
    Active = models.BooleanField(default=True)
