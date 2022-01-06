from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator
from datetime import datetime

# Create your models here.

class User(models.Model):
	login = models.CharField(max_length=30)
	birth_date = models.DateField(default=None)
	password = models.CharField(blank=True,validators=[MinLengthValidator(4)],max_length=20)
	created_at = models.DateTimeField( auto_now_add = True)
