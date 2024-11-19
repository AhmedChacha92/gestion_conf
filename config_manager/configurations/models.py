
from django.db import models
from django import forms

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
    dhcp = models.GenericIPAddressField(protocol='IPv4')
    ip_private = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
    ip_public = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
    interco = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
    
    
    class ConfigurationForm(forms.Form):
        client_name = models.CharField(max_length=100)
        dhcp = models.GenericIPAddressField(protocol='IPv4')
        ip_private = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
        ip_public = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
        interco = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
        
        def __str__(self):
            return f"{self.client_name} - {self.operator} - {self.service}"