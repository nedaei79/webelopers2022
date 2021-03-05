from django.db import models


class product(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    price = models.IntegerField()
