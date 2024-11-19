# configurations/forms.py
from django import forms
from .models import Configuration
import os
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = ['operator', 'service', 'client_name', 'dhcp', 'ip_private', 'ip_public', 'interco']
        widgets = {
            'dhcp': forms.TextInput(attrs={'placeholder': 'xxx.xxx.xxx.xxx'}),
            'ip_private': forms.TextInput(attrs={'placeholder': 'xxx.xxx.xxx.xxx'}),
            'ip_public': forms.TextInput(attrs={'placeholder': 'xxx.xxx.xxx.xxx'}),
            'interco': forms.TextInput(attrs={'placeholder': 'xxx.xxx.xxx.xxx'}),
        }
            
          
class FileSelectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FileSelectionForm, self).__init__(*args, **kwargs)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        txt_dir = os.path.join(base_dir, 'fichier txt')
        txt_files = [(f, f) for f in os.listdir(txt_dir) if f.endswith('.txt')]
        self.fields['file'] = forms.ChoiceField(choices=txt_files)
        
def create_dynamic_form(fields):
    class DynamicForm(forms.Form):
        for field in fields:
            locals()[field] = forms.CharField(max_length=255, required=False)
    return DynamicForm

class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Prénom')
    last_name = forms.CharField(max_length=30, required=True, help_text='Nom')
    username = forms.CharField(max_length=30, required=True, help_text='Nom d\'utilisateur')
    email = forms.EmailField(max_length=254, required=True, help_text='Adresse email')
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Mot de passe')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Confirmez le mot de passe')
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True, help_text='Nom d\'utilisateur ou adresse email')
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Mot de passe')
