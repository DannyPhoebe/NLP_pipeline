from django.db import models

# Create your models here.
class Consult(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=30)
	message = models.CharField(max_length=200)
