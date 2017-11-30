from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

for user in User.objects.all():
    Token.objects.get_or_create(user=user)

@receiver(post_save, sender=settings.get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print("USER CREATED!")
    if created:
        Token.objects.create(user=instance)

