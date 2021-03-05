from django.contrib.auth.models import Group
from django.db import models
from django import forms

sellers, created = Group.objects.get_or_create(name='sellers')
