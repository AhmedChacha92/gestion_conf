# configurations/views.py
from django.shortcuts import render, redirect
from .forms import ConfigurationForm
from .models import Configuration
import pandas as pd
from django.http import HttpResponse

def home(request):
    return render(request, 'base.html')

def add_or_edit_configuration(request, pk=None):
    if pk:
        config = Configuration.objects.get(pk=pk)
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
    configs = Configuration.objects.all()
    return render(request, 'list.html', {'configs': configs})

def download_excel(request):
    configs = Configuration.objects.all()
    df = pd.DataFrame(list(configs.values()))
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="configurations.xlsx"'
    df.to_excel(response, index=False)
    return response