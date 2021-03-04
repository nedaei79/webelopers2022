from django.db import models
from django import forms


class reg_form(forms.Form):
    first_name = forms.CharField()