from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class photos(models.Model):
    img = models.FileField(upload_to='apps/webframe/media')