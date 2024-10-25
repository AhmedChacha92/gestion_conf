
from django.db import models

class Configuration(models.Model):
    OPERATOR_CHOICES = [
        ('SFR', 'SFR'),
        ('Bouygues', 'Bouygues'),
        ('Orange', 'Orange'),
    ]
    SERVICE_CHOICES = [
        ('Internet', 'Internet'),
        ('Telephony', 'Telephony'),
        ('Both', 'Both'),
    ]
    operator = models.CharField(max_length=10, choices=OPERATOR_CHOICES)
    service = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    client_name = models.CharField(max_length=100)
    dhcp = models.CharField(max_length=100)
    ip_private = models.CharField(max_length=15, blank=True, null=True)
    ip_public = models.CharField(max_length=15, blank=True, null=True)
    interco = models.CharField(max_length=100, blank=True, null=True)