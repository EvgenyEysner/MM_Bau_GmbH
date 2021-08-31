from datetime import datetime

from django.core.validators import RegexValidator
from django.db import models


class Slider(models.Model):
    """
    create Slider
    """
    pass


class Contact(models.Model):
    name = models.CharField('Name', max_length=256)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=16, blank=True)  # Validator soll eine Liste sein
    email = models.EmailField('email', max_length=254)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Anfrage'
        verbose_name_plural = 'Anfragen'
        ordering = ['-created']

    def __str__(self):
        return f'Name: {self.name}'
