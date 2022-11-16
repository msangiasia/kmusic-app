from django.db import models

# Create your models here.

class User(models.Model):
	user_id =models.IntegerField(default=0)
	name = models.CharField(max_length= 100)
