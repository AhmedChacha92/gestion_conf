from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConfigurationForm, FileSelectionForm, create_dynamic_form
from .models import Configuration
import os
import re
import pandas as pd
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm

MODIFIED_FILES_DIR = 'modified_files'

def home(request):
    return render(request, 'home.html')

def select_file(request):
    if request.method == 'POST':
        form = FileSelectionForm(request.POST)
        if form.is_valid():
            selected_file = form.cleaned_data['file']
            return redirect('configurations:edit_file', filename=selected_file)
    else:
        form = FileSelectionForm()
    return render(request, 'select_file.html', {'form': form})

def edit_file(request, filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    txt_dir = os.path.join(base_dir, 'fichier txt')
    modified_dir = os.path.join(base_dir, MODIFIED_FILES_DIR)
    if not os.path.exists(modified_dir):
        os.makedirs(modified_dir)
    template_path = os.path.join(txt_dir, filename)
    with open(template_path, 'r') as file:
        content = file.read()

    fields = re.findall(r'\$(\w+)\$', content)
    DynamicForm = create_dynamic_form(fields)

    if request.method == 'POST':
        form = DynamicForm(request.POST)
        if form.is_valid():
            modified_content = content
            for field in fields:
                modified_content = modified_content.replace(f'${field}$', form.cleaned_data[field])
            modified_filename = f"{filename.split('.')[0]}_modified.txt"
            modified_path = os.path.join(modified_dir, modified_filename)
            with open(modified_path, 'w') as modified_file:
                modified_file.write(modified_content)
            return redirect('configurations:file_list')
    else:
        form = DynamicForm()

    return render(request, 'edit_file.html', {'form': form, 'content': content, 'filename': filename})

def file_list(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    modified_dir = os.path.join(base_dir, MODIFIED_FILES_DIR)
    files = os.listdir(modified_dir)
    return render(request, 'file_list.html', {'files': files})

def add_or_edit_configuration(request, pk=None):
    if pk:
        config = get_object_or_404(Configuration, pk=pk)
    else:
        config = None

    if request.method == 'POST':
        form = ConfigurationForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            return redirect('configurations:list')
    else:
        form = ConfigurationForm(instance=config)

    return render(request, 'form.html', {'form': form})

def list_configurations(request):
    operator = request.GET.get('operator')
    service = request.GET.get('service')
    dhcp = request.GET.get('dhcp')

    configs = Configuration.objects.all()

    if operator:
        configs = configs.filter(operator=operator)
    if service:
        configs = configs.filter(service=service)
    if dhcp:
        configs = configs.filter(dhcp=dhcp)

    return render(request, 'list.html', {'configs': configs})

def download_excel(request):
    configs = Configuration.objects.all()
    df = pd.DataFrame(list(configs.values()))
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="configurations.xlsx"'
    df.to_excel(response, index=False)
    return response

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('configurations:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('configurations:home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('configurations:home')
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset.html', {'form': form})