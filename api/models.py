from django.db import models
from datetime import datetime

# Create your models here.
class Project(models.Model):
    date = models.DateTimeField(default=datetime.now(), blank=True)
    project_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads', blank=True)
