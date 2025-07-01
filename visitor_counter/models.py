from django.db import models

# Create your models here.
class VisitorCounter(models.Model):
    count=models.IntegerField(default=0)
