import os
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import Token

from api.storage import OverwriteStorage


#TODO: maybe move auth token receiver to an 'accounts' app in future if account related things get more complicated.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def customImagePath(instance, filename):
    """
    Names the image file to be saved after the model instance.name and returns the path.
    Meant to be passed in to upload_to parameter for File or ImageFields.
    """
    ext = filename.split('.')[-1]

    if instance.name:
        filename = "{}.{}".format(instance.name.lower(), ext)
    
    return os.path.join('images', filename)

#models
class Project(models.Model):
    date        = models.DateTimeField(default=timezone.now, blank=True)
    name        = models.CharField(max_length=50)
    slug        = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=500)
    text        = models.CharField(max_length=5000)
    image       = models.ImageField(storage=OverwriteStorage(), upload_to=customImagePath, blank=True, null=True)
 
    def save(self, *args, **kwargs):
        if not self.slug:
            # Create a lower-case, underscored name (slug) for use in URLs
            self.slug = self.name.replace(' ', '_').lower()
            print("SAVED PROJECT SLUG!")
        super(Project, self).save(*args, **kwargs)

