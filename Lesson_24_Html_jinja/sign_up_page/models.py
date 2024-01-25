from django.db import models


class SignUpPage(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20, null=False)
