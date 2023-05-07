from django.db import models

# Create your models here.
class Module(models.Model):
    module_code = models.CharField(max_length=255)
    module_name = models.CharField(max_length=255)
    