# configurations/urls.py
from django.urls import path, include
from . import views

app_name = 'configurations'

urlpatterns = [
    path('', views.home, name='home'),
    path('select_file/', views.select_file, name='select_file'),
    path('edit/<str:filename>/', views.edit_file, name='edit_file'),
    path('file_list/', views.file_list, name='file_list'),
    path('add/', views.add_or_edit_configuration, name='add'),
    path('edit/<int:pk>/', views.add_or_edit_configuration, name='edit'),
    path('list/', views.list_configurations, name='list'),
    path('download_excel/', views.download_excel, name='download_excel'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
]