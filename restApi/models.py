from django.db import models

class User(models.Model):
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    isVerified = models.BooleanField()
    superuser = models.BooleanField()


    def __str__(self):
        return self.username
