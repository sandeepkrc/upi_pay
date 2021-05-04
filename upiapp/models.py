from django.db import models

class Pay(models.Model):
	amount = models.CharField(max_length=20)
	paytype = models.CharField(max_length=30)
