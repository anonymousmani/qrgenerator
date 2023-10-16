from django.db import models

# Create your models here.
class qr(models.Model):
    text = models.CharField(max_length=50)
