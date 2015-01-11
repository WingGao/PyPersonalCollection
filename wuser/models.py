from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    last_login = models.DateTimeField(auto_created=True)