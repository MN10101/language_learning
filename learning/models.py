from django.db import models

# learning/models.py
from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

