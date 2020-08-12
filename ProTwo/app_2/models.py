from django.db import models

# Create your models here.
class USERS(models.Model):
    f_name = models.CharField(max_length=60)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
