# configurations/forms.py
from django import forms
from .models import Configuration

class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = ['operator', 'service', 'client_name', 'dhcp', 'ip_private', 'ip_public', 'interco']