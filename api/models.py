from datetime import datetime

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#TODO: maybe move auth token receiver to an 'accounts' app in future if account related things get more complicated.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

#models
class Project(models.Model):
    date = models.DateTimeField(default=datetime.now(), blank=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads', blank=True)
