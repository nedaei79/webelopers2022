from django.contrib.auth.models import Group
from django.db import models


class product(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    price = models.IntegerField()

sellers, created = Group.objects.get_or_create(name='sellers')
