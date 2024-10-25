from django.urls import path
from . import views

app_name = 'configurations'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_or_edit_configuration, name='add'),
    path('edit/<int:pk>/', views.add_or_edit_configuration, name='edit'),
    path('download_excel/', views.download_excel, name='download_excel'),
    path('list/', views.list_configurations, name='list'),
]